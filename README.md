# Gnoppix Suite — i18n resources

This folder holds **all user-visible strings** of the Gnoppix Suite desktop app
(Email, Calendar, People, Tasks). It is designed so anyone can improve a
translation by editing a JSON file and opening a pull request — no programming
knowledge required.

## Files

| File    | Language            |
|---------|---------------------|
| en.json | English (canonical) |
| de.json | German              |
| es.json | Spanish             |
| fr.json | French              |
| ja.json | Japanese            |
| zh.json | Simplified Chinese  |

`en.json` is the source of truth. Every other file must contain **exactly the
same keys** in the same order. Missing keys fall back to English automatically,
so a partial translation never breaks the app.

## Key naming

Keys are grouped by module and use dots:

- `app.*` — window chrome, theme, app title
- `module.*` — the four module names in the left rail
- `common.*` — shared words (Save, Cancel, Delete, …)
- `time.*`, `dates.*` — relative times, month/weekday names
- `mail.*`, `compose.*`, `settings.*` — Email module
- `people.*` — contacts module
- `tasks.*` — tasks module
- `cal.*` — calendar module

## Placeholders

Some values contain `{name}`-style placeholders, e.g.

```json
"mail.sendFailed": "Send failed: {detail}",
"people.labelApplied": "Label “{label}” applied to {n} contact{p}"
```

Keep every `{...}` token **exactly as written** (same spelling, same braces).
You may move it inside the sentence where the grammar requires it.
`{p}` is an optional plural suffix ("s" / ""), translate the whole sentence
naturally instead.

## Do not translate

- Proper nouns / product names: Gnoppix, Gnoppix Suite, Gnoppix Calendar
- Protocols and formats: IMAP, POP3, SMTP, STARTTLS, SSL/TLS, HTML, vCard, CSV, ICS, OpenPGP, GPG, PGP, GnuPG
- Message prefixes `Re:` and `Fwd:` (email compatibility)
- Symbols embedded in values: ↓ ↑ → ★ ⚑ ✕ ✓ · …
- URL / address examples such as `imap.example.com` or `a@b.c, d@e.f`

## Special arrays

- `dates.months` / `dates.monthsShort` / `dates.weekdays` — 12/12/7 items,
  used for calendar headers.
- `people.csvHeaders` — used for both exporting **and** importing contact
  CSV files, so these column names must stay meaningful and stable
  (import also accepts the English headers).

## Standard mail folders

Server folder names (Inbox, Sent, Drafts, Trash, Junk, Archive) are translated
for display through the `mail.folder*` keys. Custom folders keep their real name.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: edit **one** language
file, keep all keys and placeholders intact, and open a pull request. Run
`python3 check.py` locally to verify your file — it checks key parity and
placeholders.
