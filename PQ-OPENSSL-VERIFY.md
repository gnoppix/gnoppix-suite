# Verifying a PQ certificate bundle with OpenSSL

External verification of the bundle produced by Settings → Post-Quantum → **Export**
(`pqcert_export`). All commands below were run and confirmed on a Gnoppix Suite
host with **OpenSSL 3.6.5**, which natively supports FIPS 204 (ML-DSA) and
FIPS 203 (ML-KEM) in its default provider — OpenSSL **3.5 or newer** is
required; older versions parse the PEM but cannot verify the signatures.

## 1. Where the export lands

- File name: `<last-16-hex-of-fingerprint>.pq.pub.pem`
  (e.g. `42c78388023bce54.pq.pub.pem`).
- Location: the system **download directory** (XDG `XDG_DOWNLOAD_DIR` from
  `~/.config/user-dirs.dirs`). On this desktop it is set to `$HOME`, so
  exports appear directly in the home directory. This is the same mechanism
  used by the OpenPGP `.asc` export.
- Content: **public material only** — two concatenated X.509 certificates:
  the ML-DSA-65 signing cert and the ML-KEM-768 encapsulation-key cert.
  Private seeds stay in the OS keyring (`pqcert-dsa-<id>` / `pqcert-kem-<id>`);
  the full identity additionally lands in the backup folder `~/.gnoppix-suite/`
  (section 1a).

## 1a. The identity backup folder (`~/.gnoppix-suite/`)

Every generate/export also writes `~/.gnoppix-suite/` (0700):
`<label>-<fp16>.pq.bak` (JSON: certs + PKCS#8 keys), `.pq.pub.pem` (the bundle
above), `.pq.dsa.key.pem` / `.pq.kem.key.pem` (0600) and — opt-in —
`.pq.pass` (0600). With a backup passphrase the key files are PKCS#8 PBES2
(`BEGIN ENCRYPTED PRIVATE KEY`, scrypt + AES-256-CBC), OpenSSL ≥ 3.5 reads
them with the passphrase:

```sh
openssl pkcs8 -in ~/.gnoppix-suite/<label>-<fp16>.pq.dsa.key.pem -passin pass:'YOUR-PASSPHRASE'
```

Without a passphrase the key files are plain PKCS#8 (`BEGIN PRIVATE KEY`) —
just file permissions protect them. `openssl pkeyutl`-level ML-DSA
verification of the exported certificates works exactly as in sections 2–4
(the PEM bundle in the backup folder is byte-identical to the download).

## 2. Inspect the signing certificate (first cert)

```sh
F=~/42c78388023bce54.pq.pub.pem
openssl x509 -in $F -noout -subject -dates -ext keyUsage,subjectAltName
```

```
subject=CN=<label>
X509v3 Key Usage: critical
    Digital Signature
X509v3 Subject Alternative Name:
    email:<address>
```

`-noout -text` shows the full dump: `Signature Algorithm: ML-DSA-65`,
`Public Key Algorithm: ML-DSA-65`, 10-year validity.

## 3. Extract the KEM certificate (second cert)

`openssl x509` only reads the *first* certificate in a file, so slice the
second PEM block out first:

```sh
awk '/-----BEGIN CERTIFICATE-----/{n++} n==2' $F > /tmp/kem.pem
openssl x509 -in /tmp/kem.pem -noout -text
```

Shows `Public Key Algorithm: ML-KEM-768`, Key Usage `Key Encipherment`,
`CA:FALSE`, same subject/SAN as the signing cert.

> Note: use the `awk` slice above, not `csplit` — splitting on the
> `-----END CERTIFICATE-----` line can drop the END marker and produce
> unparseable chunks.

## 4. Cryptographically verify the signing certificate (self-signed)

```sh
openssl verify -partial_chain -trusted $F $F
# → /home/<user>/42c78388023bce54.pq.pub.pem: OK
```

This performs a real ML-DSA-65 signature check against the certificate's own
public key.

## 5. Cryptographically verify the KEM certificate's signature

The KEM cert is signed by the identity's ML-DSA-65 key but is not chained via
a CA — plain `openssl verify` on it fails with `invalid CA certificate` /
`key usage does not include certificate signing`. That is X.509 chain
**policy** (the bundle is deliberately two leaf certs under one identity,
`CA:FALSE`), not a broken signature. Check the signature directly:

```sh
openssl x509 -in $F -noout -pubkey > /tmp/pub.pem          # identity's ML-DSA-65 public key
openssl asn1parse -in /tmp/kem.pem -out /tmp/kem.der       # DER + offset tree
```

Read the `d=1` rows of the asn1parse tree (they change per certificate —
for the example bundle they were):

```
4:d=1  hl=4 l=1405 cons: SEQUENCE     ← TBSCertificate
1413:d=1 hl=2 l=11 cons: SEQUENCE     ← SignatureAlgorithm
1426:d=1 hl=4 l=3310 prim: BIT STRING ← signature value
```

Extract the signed bytes and the signature, then verify:

```sh
dd if=/tmp/kem.der of=/tmp/tbs.der bs=1 skip=4   count=1409    # TBSCertificate DER
dd if=/tmp/kem.der of=/tmp/sig.bin bs=1 skip=1431 count=3309   # BIT STRING payload minus unused-bits byte
openssl pkeyutl -verify -pubin -inkey /tmp/pub.pem -in /tmp/tbs.der -sigfile /tmp/sig.bin
# → Signature Verified Successfully
```

## 6. Cross-check the fingerprint against the app

```sh
openssl x509 -in $F -noout -fingerprint -sha256
# → SHA256 Fingerprint=97:81:32:BB:...:42:C7:83:88:02:3B:CE:54
```

The app stores exactly this SHA-256 of the certificate in the `pq_certs`
table (`SELECT id,label,fingerprint FROM pq_certs;`, DB at
`~/.local/share/org.gnoppix.calendar/mail.db`), and the export filename tail
is its last 16 hex digits — openssl, the DB and the filename must all agree.

## 7. Validity window

```sh
openssl x509 -in $F -noout -checkend 31536000   # nonzero exit if expiring < 1 year
```

Certificates are valid 10 years from generation; regenerate from the
Post-Quantum tab before expiry.
