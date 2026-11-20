# Gnoppix Suite — User Guide

Gnoppix Suite is a desktop suite for Linux (XFCE and any X11 desktop) with seven
modules behind a left app-switcher rail: **Email** (default), **Calendar**,
**People**, **Tasks**, **Recordings**, **AI** and **VPN/TOR**.

---

## 1. Getting started

### Install
- From the `.deb`: `sudo apt install ./gnoppix-suite_<version>_amd64.deb` (current: 0.1.37)
- The app appears in your desktop menu as **Gnoppix Suite**, or start it from a
  terminal with `gnoppix-suite`.

### First launch
The rail on the far left switches modules. Your last-used module and theme are
remembered between launches. Language is detected from your system; change it any
time in **Email → settings (gear) → General**.
If the interface ever hits an unexpected error, a recovery card appears instead of
a blank window — press Reload; your mail and data are untouched.

---

## 2. Doc (documentation & links)

The Doc module — the last item on the rail (document icon), just below VPN/TOR — gathers documentation,
about and support links. Every entry opens in your system **default browser**.

This applies **everywhere in the app** (0.1.37): any link you click — inside an
email body, a calendar entry, a note, a signature, a messenger message or an AI
answer — always opens in your system default browser (mailto/tel links go to
your system handlers). The Suite itself never loads a web page inside its own
window.

The page also states the licensing terms: the Suite is not a free application — it is
exclusive to Gnoppix Members and enterprise email users (import your license file under
**Settings → License**). An unlocked version is available for **US $5.78**; the Suite is
designed specifically to run on Gnoppix Linux — it may also run on other distributions.

- **Project homepage** — the Gnoppix Suite project page (gnoppix.me).
- **Order 6-month email subscription** — order the 6-month email subscription via Ko-fi.
- **Get a free account with @gnoppix.me email** — the Gnoppix landing page
  (landing.gnoppix.com).
- **Free webmail access with your Gnoppix.me account** — open webmail in your
  browser (webmail.gnoppix.org).
- **Gnoppix homepage** — the main Gnoppix site (gnoppix.org).
- **Gnoppix user documentation** — this guide on the Gnoppix wiki
  (Configuration → Gnoppix Suite → User guide).
- **Report a bug** — opens the gnoppix-suite issue tracker on GitHub.
- **Suggest something to implement** — same tracker, for feature requests.
- **Add your own language** — the GitHub repository, where you can contribute a
  translation of the interface.
- **Become a sponsor** — support Gnoppix (gnoppix.org/sponsor).

## 3. Today (day summary)

The **Today** entry at the top of the left rail gives you the day at a glance:

- **Calendar today** — every calendar entry that falls on today (all-day
  entries first, then timed ones; entries spanning several days are included).
  Click an entry to open it directly in the calendar, in its month, with the
  detail card open.
- **Tasks due today** — your open tasks with a due date today. Tick the box to
  mark one done; click the row to jump to the task list.
- **Top 5 flagged emails** — the five newest flagged (marked) emails across all
  your accounts. Click one to open it in Email.
- **Top news** — the three top Google News headlines for your country. The
  country follows your app language (German → Deutschland, English → United
  States …) and you can change it in the card's country selector — your choice
  is saved. Click a headline to open it in your default browser. The
  headlines are fetched by the app itself (nothing remote ever loads inside the
  app window).
- **Gnoppix Forum — latest** — the three newest topics from
  forum.gnoppix.org; click to open in your browser.

News and forum entries are cached locally (an unencrypted file — titles and
links only): Today opens instantly even offline, the app refreshes the feeds
in the background every 18 minutes, and the ⟳ button in the Today header
updates news, forum, tasks and flagged emails on demand.

The summary keeps itself current as mail, tasks and calendar change.

## 4. Email (default module)

Modern style layout: folder tree | message list | reading pane. The reading pane
can sit on the right or at the bottom (layout toggle in the toolbar).
In dark theme, mail-declared colors inside HTML messages (white backgrounds from
provider "security alert" mails, for example) are flattened to the app's dark
palette so text stays readable; links remain blue and light theme shows the
sender's own colors exactly as sent.

### Add an account
1. Open **Settings** (gear icon in the mail toolbar) → **Accounts** tab → **Add account**.
2. Enter display name and email address. The **Password** box sits in the Incoming
   section next to its Username/Auth Type — one keyring password signs you in for
   both directions.
3. Press **Detect** — the suite tries known providers (Gmail, Outlook/Hotmail,
   Yahoo) and then generic candidates for your domain in order:
   `imap.<domain>`, `mail.<domain>`, `<domain>` on port 993 (IMAP over SSL) or
   995 (POP3 over SSL), with outgoing `smtp.<domain>`:465 (SSL) or
   `mail.<domain>`:587 (STARTTLS). Each candidate is tested live before it is kept.
4. If detection is not right, set the servers manually: protocol IMAP or POP3,
   host, port, and TLS mode (`imaps` / `starttls` / `none`, same for SMTP).
   Incoming and Outgoing each show a Username + Auth Type; the Outgoing username is
   optional — leave it empty to sign in to SMTP with the incoming username (only the
   server settings differ per direction, and Test verifies both).
5. **Test** verifies incoming + outgoing connections before saving.

Passwords are stored only in your operating system's secure keyring — never in
the app's database. If your desktop asks to unlock a keyring on first save, allow it.

### Reading and organizing mail
- Click a message card to open it in the reading pane; unread/flagged filters and
  sorting are in the toolbar, search box at the top of the list.
- Mark read/unread, flag, archive, move to another folder, or delete. Deleting
  moves the message to Trash. You can also right-click a message in the list to
  get a **Delete** menu — it moves it to Trash the same way; the menu closes with
  a click elsewhere or Escape. When you delete the email that is open, the next
  email in the list opens automatically — the card that took the deleted one's
  place (or the previous one if it was at the end).
- Right-click a **folder** in the folder list to get **Mark all as read** /
  **Mark all as unread** — every message in that folder is marked and the read
  state is synced back to the mail server. On the Trash folder the menu also
  shows **Empty Trash**, which deletes all messages in it. The menu closes with
  a click elsewhere or Escape.
- While the app runs, the **system tray** icon shows a red **unread-count**
  badge (unread messages in each account's Inbox, summed over accounts), and
  the window title carries the same number. It updates whenever the mail list
  refreshes; clicking the tray icon brings the window forward.
- Emails from senders already in your address book are highlighted: the sender's
  name in the list and the From row in the reading pane are shown in orange with
  a **VIP** chip. Click **VIP** to open that contact in People directly. For a
  sender who is not yet in your address book, the reading pane shows
  **+ Contact** — one click adds them, and their emails turn VIP from then on.
- **Flag** an email to turn it into work: it creates a task and a calendar
  entry from the email's content (a due day written in the subject/body is
  used; otherwise today). The task lands in the task list you last opened in
  Tasks and shows a small mail chip; the
  calendar entry has an **Open email** button — either jumps back to the
  original message. Delete the email for good (from Trash, or POP3 delete) and
  the task is completed and the calendar entry is removed automatically.
- **AI Wizard** (dropdown in the mail ribbon, left of **Reply**): **Summarize**
  and **Translate** only. Choosing an entry only selects it — press **Go** to
  start. For Translate, the target language picker appears beside the wizard;
  pick the language *first*, then Go (nothing runs until you press Go). While
  the AI works, an **"AI in progress"** card shows centered over the window and
  disappears when the answer is complete or the run errors. The answer streams
  into a panel under the header. (Classify, Spam check, Suggest tags and
  Task/Event extraction stay available in the AI module's Actions tab.)
  Answers are cached per email (and, for Translate, per language): a stored
  summary reappears with a *cached* chip when you reopen the email, **Regenerate**
  re-asks the model. Actions need the message body, so they activate after the
  body is fetched.
- Folders: Inbox, Sent, Drafts, Junk, Trash, Archive plus any custom folders on
  your server. **Create folder** and **Empty folder** are in the folder pane menu.
- Only the newest messages sync per account (default: last 50 new messages per
  folder per sync) to keep startup fast.

### Writing mail
- **Compose** opens a rich editor: bold, italic, lists, links, inline images.
- Attach files by clicking or by dragging them into the composer; attachments are
  staged until you send.
- A message that arrives with files shows an **Attached files:** field below the
  Date in the reading pane (marked with a paperclip). Each file name is a button:
  clicking it saves the file into your `Download/emails` folder — original name,
  with `-1`, `-2` … suffixes if a file of that name already exists — and a
  notification confirms where it was saved. Attachments inside encrypted mail
  appear once the message is opened (encrypted attachments are recovered
  automatically).
- Your signature (Settings → Signatures tab, plain text or HTML per account) is
  appended automatically when composing or replying.
- Sending a message without pressing Send saves it as a draft automatically;
  drafts appear in the Drafts folder and can be resumed, discarded (right-click or Del),
  or dragged onto any folder to save them as a real message — IMAP accounts store it on the
  server in that folder, POP3 accounts keep it locally.
- **Replies keep the account they belong to.** With several accounts, a Reply, Reply all
  or Forward is sent from the address that message arrived at — the account whose folder it
  landed in — not from whichever account is selected in the sidebar. Mail that reached you
  through a relay (the sender address differs from your own) is answered from the receiving
  account, so identities never get mixed up. Each account's Drafts folder lists only its own
  drafts and labels them with the address they will be sent from (Draft · name@domain).
  If a send fails (server unreachable, missing password, …) the draft stays where it is,
  marked with ⚠, and an error toast names the reason — open the draft and press Send
  again to retry.
- You decide otherwise: the account selector at the top of the composer switches the sending
  identity, and what you pick there is what gets used — including which OpenPGP or
  post-quantum key signs and encrypts the message.
- The **To** field suggests contacts you use often (from the People module).
- Mail you send is marked as yours: every outgoing message carries the header
  `X-Mailer: Gnoppix Secure eMail <version>`, including replies, forwards, attachments and
  encrypted or signed mail, and the copy kept in your Sent folder carries it too.

### Encrypted mail (OpenPGP)
In Settings → **OpenPGP** tab you can import an existing GnuPG key, generate a
new one, export or delete keys, and pick per account which key to use and when:
sign only, encrypt only, or sign+encrypt. Sent messages get a green verified
badge or a lock badge in the reading pane; incoming signed messages are verified
automatically. If your secret key has a passphrase, two modes are available.
Default: the app uses your system GnuPG pinentry window — you type the
passphrase once per login session (GnuPG's agent caches it), not on every app
start. Optional: save it in the same tab (**Save passphrase** — stored only in
the OS keyring) for fully automatic decrypt/sign with zero prompts; messages
fetched earlier that still showed the armored block then decrypt the next time
you open them.

### Automatic sync
Accounts sync automatically every 15 minutes by default (per-account interval is
editable in the Accounts tab). **Sync now** forces an immediate check. Desktop
notifications for new mail can be turned on/off in the General tab.

---

## 5. Calendar

Month and Week views, dark or light theme (moon/sun button on the rail). The rail shows the
installed app version (e.g. `v 0.1.4`) under the theme button — always the version you are running.

### Add calendars
Open **Sources** (toolbar) → choose a type:
- **Google Calendar (public)** — paste the calendar address of any public Google
  calendar (`…/calendar/ical/<id>/public/basic.ics`).
- **Private Google calendar** — in Google Calendar settings → *Integrate
  calendar*, copy the *secret address in ICS format* and add it as a custom ICS
  source. Keep that URL private; anyone who has it can read your calendar.
- **Gnoppix mail account** — pick one of your configured mail
  accounts; the suite connects to its CalDAV calendar directly, so events you
  create here also appear on your server (and vice versa).

Each calendar gets a color and an enable/disable switch in the sidebar. Removing
a source removes its cached events locally (never deletes anything on the server).

### Events
- Click a day (or **Create**) to add an event: all-day or timed, with recurrence
  (daily / weekly / monthly / yearly).
- Local "My Events" calendar is fully editable; CalDAV calendars are editable too
  (changes sync to the server); imported ICS feeds are read-only.
- **Delete is two-step**: first click arms the button ("Confirm delete?"), a
  second click deletes. This protects you from accidental one-click deletion.

---

## 6. People (address book)

Modern-style address book: directory sidebar (All contacts / Favorites /
Labels) on the left, a cards list with sortable column headers in the middle, and a
contact **Details** pane on the right — the same three-pane layout as Modern's
Address Book.

- Column headers are clickable to sort (▲/▼); the ▾ menu toggles extra columns
  (Nickname, Address, Title, Department, Company, Labels, Birthday), like
  Modern's "Columns" menu. Default visible: Name, Email, Phone.
- Selecting a contact shows Modern-style detail sections: Email addresses,
  Phone numbers (Home/Work/Mobile with type labels), Addresses, Notes, Websites,
  Other (birthday/anniversary) — plus the **Write** button that jumps to the mail
  composer and an Edit button.
- Editing opens a Modern-style vCard form in the details pane (fieldsets:
  name/nickname/display name, email, phone Home/Work/Mobile, street/city/state/ZIP/
  country, title/department/company/website/birthday/anniversary, notes, labels).
- A **Frequent contacts** row (like Modern's) sits above the list and shows the
  people you email most; until then it says "No frequent contacts yet." Contacts you
  email often get a ↻ "frequent" badge and float to the top of the To-field
  suggestions in the composer.
- Reading pane has a quick **Add contact** button for new senders.
- **Import / Export** work with CSV files and vCards (`.vcf`, Modern fields:
  NICKNAME, TITLE, ORG, URL, TEL;TYPE=WORK/CELL, ADR) — CSV headers follow your
  app language.
- A contact's **Email** action jumps straight to the mail composer.

---

## 7. Tasks

Modern-style task tree: lists on the left, filter bar, fulltext search,
quick-add bar, drag to reorder.

- Click a task title to open the details panel: title, notes (details), start
  date, due date, priority. The notes box grows to show the FULL text and
  auto-saves — switching tasks, closing the panel or quitting flushes pending
  text, so typed details are never lost. List rows truncate long titles, so a
  newly created task copies its **full title into DETAILS** (0.1.34) — the whole
  text is always readable there; existing empty-notes tasks got the same copy
  once at update, and clearing DETAILS intentionally keeps it cleared. New tasks
  start with the start date set to their creation date (clear it with "Clear
  date" if unwanted).
- Multiple lists ("My Tasks" always exists); add subtasks under any task.
- Filters: All, Today, Next Seven Days, Not Started, Overdue, Completed, Incomplete —
  same semantics as Modern's "Filter Tasks". The chosen filter is remembered.
- Search box filters tasks by title and notes across the active list. Priority
  follows Modern values (None / Low / Normal / High).
- Start date and due date (date + optional time), notes; overdue tasks are marked red.
- Completed tasks collapse into a "Completed" group you can expand (in the All filter).
- Deleting a parent task deletes its subtasks. Drag top-level tasks to reorder while
  in the default due-date order under the All filter.

---

## 8. Notes

Colored note cards on the rail entry **Notes** below Tasks — the Suite port of
the classic sticky-notes app, kept inside the Suite so your notes live in the
same encrypted-capable database as your mail and tasks.

- **New note** creates a blank colored card; new cards cycle through 8 colors
  (yellow, pink, blue, green, purple, orange, red, slate). Change a card's
  color anytime with the swatches at its bottom.
- Type straight into the card — the text saves automatically when you leave
  the field. Click rendered text to edit it again.
- Line conventions: `- [ ]` and `- [x]` render as clickable checkboxes
  (click to tick/untick), a leading `- ` renders as a bullet. Inside a line,
  **bold**, *italic* and `monospace` render inline.
- **Pin** moves a note to the front; unpinned notes sort by most recently
  edited.
- **Duplicate** copies a card; **Delete** asks for confirmation first.
- The search box filters cards by title and body.
- Notes are stored in the Suite's mail database (see "Where your data lives"),
  so they follow the same backup/encryption story as mail and tasks.

---

## 9. Messenger

The rail carries a **Messenger** entry below Notes: the Gnoppix **Add**
post-quantum messenger, built into the Suite with a Signal-style chat UI. The
Suite talks to your local `add` command-line messenger — your keys and the
network protocol stay in the CLI, and the Suite never contacts any messenger
server.

- **First start** — Create your Add identity: choose a vault passphrase (at
  least 16 characters with upper, lower, digit and symbol; it cannot be
  recovered, so store it safely). Tick *Remember in system keyring* and later
  starts unlock transparently; *Forget stored passphrase* removes that copy.
- **Loading** — while the identity and local listener start up, a centered
  **"Loading messenger…"** card with a spinner shows in the middle of the
  window; it disappears as soon as the module is ready (or shows the create /
  unlock screen instead).
- **Locked screen** — enter the vault passphrase to unlock; the lock button
  seals the vault and stops the listener.
- **Null ID display** — full Null IDs are shown in readable monospace (your own
  ID at the top of the sidebar, unnamed conversations, and the chat header).
  Click your ID or a peer's ID to copy it to the clipboard, so IDs can be
  shared and verified without any shortened, unreadable abbreviation.
- **Contacts** — **+ Add contact** takes a peer's Null ID and its safety
  fingerprint (hex, from their `add id` output); an optional display name is
  stored locally via `add alias`. A green dot shows peers currently online
  (status refresh in the chat header).
- **Chat** — Signal-style timeline: day headers, grouped consecutive messages,
  sent-status ticks. Enter sends, Shift+Enter makes a new line; drafts persist
  per conversation. The *Expires* picker sets message TTL (2h / 24h / 7d /
  14d). The green LED in the sidebar starts/stops the background listener that
  receives incoming messages live. Ctrl+K searches conversations, Alt+↑/↓
  switches between them.

Without the `add` package installed the module shows a clear notice; browser
preview (`npm run dev`) shows a read-only demo.

---

## 10. Recordings

Voice memos, reachable from its own rail button below Messenger.

- **Record** captures from the microphone (Opus/WebM by default). A live level
  meter shows the waveform while recording and a red timer counts elapsed time.
- **Pause / Resume** during a recording; **Stop** saves it automatically. Files
  are stored in the app data directory (`recordings/`) and never overwrite an
  existing name — duplicates get numbered like Sound Recorder does.
- Each entry shows its name, date ("today", "yesterday", "N days ago"),
  duration and a cached waveform. **Play** streams it back (click again to
  stop), **Rename** changes the file, **Delete** removes recording and file.

---

## 11. AI

AI-style assistant for mail and text work, in its own rail button below
Recordings. Works with local models (Ollama is the default — no account or API
key needed) as well as OpenAI, Anthropic, Google Gemini and any
OpenAI-compatible server (LM-Studio, vLLM…).

- **Chat**: streamed multi-turn conversation with your configured model.
- **Actions**: AI's prompt library over any text — rewrite polite /
  formal, proofread, summarize into bullets, classify tone, spam check,
  suggest tags, translate, draft a reply. Results stream in place.
- **Extract**: paste an email or note; the AI returns structured JSON
  (AI's get_task / get_calendar_event prompts) and one click turns it
  into a real Task or Calendar event.
- **On a message**: the mail ribbon's **AI Wizard** dropdown (left of Reply,
  see Email §4) — **Summarize** and **Translate** run directly on the open
  email (select, pick language, press Go), no copy-paste; answers are cached
  per message (Translate per language) and shown again on reopen.
- **Transcribe**: voice memos from the Recordings module can be transcribed
  with a multimodal model; transcripts are saved per recording.
- Settings: provider, host, model picker (loads the server's model list),
  API key (stored in the OS keyring, never in the database), num_ctx and
  thinking-mode toggles, a keep-in-RAM toggle (Ollama only — pins the model so
  the first chat after startup is instant and no mid-session reload happens;
  the pin is released automatically when the app closes) and an Unload model
  button to free the RAM on demand.
- **Connect test** (right side of the model row): checks the host, the chosen
  model and — for cloud providers — the API key; the button turns **green** on
  success, **red** with the error text on failure, and its label changes to
  *Re-Test* after the first test. Editing host or model resets it.
- While any AI request is in flight the mouse shows the system **wait/clock
  cursor** across the whole window, so long generations are obviously busy.
- **Prompts tab** (the AI "Manage prompts" section): the built-in
  prompt library is **editable** — change a built-in's text and it is used
  everywhere (an "edited" badge marks it; *Reset* restores the shipped text),
  and you can create, edit or delete your **own prompts**. Click a
  placeholder chip to insert it where the cursor sits — placeholders like
  `{%mail_subject%}` or `{%mail_text_body%}` receive the email's data when the
  prompt runs; a prompt that uses placeholders but none carrying the message
  gets a warning so the email actually reaches the model. Saved prompts appear
  immediately in this tab's Actions dropdown and in the mail **AI Wizard**.

---

## 12. VPN / TOR

The VPN module runs GnoppixCTL, the Gnoppix Tor/VPN client, as a normal
application window (it must be installed at `/opt/gnoppixctl/GnoppixCTL`).
Opening the module starts GnoppixCTL and brings it to the foreground; if it is
already running — started here or from the desktop menu — it is simply brought
to the front, never launched a second time.

Switching to another module leaves GnoppixCTL running. In the VPN toolbar you can
**Bring to front** (show its window again) or **Stop** (close the GnoppixCTL
window). Closing the suite does not close GnoppixCTL — close it via its own
window button when you want it gone.

---

## 13. Post-quantum identities

Settings → **Post-quantum** manages post-quantum identities — a quantum-resistant
key type based on the standardized algorithms FIPS 204 (ML-DSA, signing) and
FIPS 203 (ML-KEM, encryption). Each identity is a pair of certificates: a signing
certificate and an encryption (KEM) certificate. Private keys are kept only in
the system keyring, never in the mail database.

- **Generate identity** — give a name, your email and optionally a backup
  passphrase (at least 8 characters); the certificate pair is created, listed
  and a portable backup is written automatically (see *Backup and restore*).
- **Export / Import** — export copies your identity's PEM bundle (share it so
  others can encrypt to you); import a contact's PEM bundle to be able to
  encrypt for them. Imported certificates are validated on import, marked
  “imported” and are public-only.
- **Backup and restore** — generating or exporting an identity writes a
  portable backup into `~/.gnoppix-suite/`: `<name>-<fingerprint>.pq.bak`
  (both certificates + your private keys in standard PKCS#8 format), the
  public bundle as `.pq.pub.pem`, the two key files `.pq.dsa.key.pem` /
  `.pq.kem.key.pem`, and — when you tick *Also save the passphrase* — the
  passphrase itself as `.pq.pass`. With a passphrase the keys are encrypted
  (OpenSSL 3.5+ or any FIPS 204/203 tool can read them with it again), so the
  same identity can be reused in other applications; without one the key
  files are unencrypted (file permissions 0600). **Export** downloads the
  public PEM and refreshes that backup, automatically reusing a saved
  passphrase. **Restore backup** (file picker + optional passphrase) reads a
  `.pq.bak` back in: the certificates are verified and the keys return to the
  system keyring — a lost keyring no longer means a lost identity. Keep the
  folder private: a saved passphrase beside its encrypted backup cancels the
  encryption for anyone who can read the folder, so delete the `.pq.pass`
  before moving a backup elsewhere.
- **Mail integration** — in Settings → **Mail → account**, set *Post-quantum
  mail encryption* to **Sign**, **Encrypt** or **Sign + Encrypt** (exactly the
  OpenPGP modes, just with post-quantum ciphers; PQ overrides the OpenPGP mode
  when set) and optionally pin a specific **PQ identity** instead of Auto
  (match account email). Outgoing messages are handled automatically:
  *Sign* keeps your text readable and appends a post-quantum signature block;
  *Encrypt* / *Sign + Encrypt* seal the body into a PQ envelope — every
  recipient must have an imported PQ certificate; if one does not, the app
  automatically falls back to OpenPGP encryption using that recipient's GPG
  key (and only fails if neither cipher is available). Either way, mail that
  was encrypted with the *older* GPG method keeps opening transparently —
  the app detects per message which cipher was used, so GPG-era and PQ-era
  mail coexist in the same account. Incoming mail is opened and verified
  automatically, showing the same lock/verified badges as OpenPGP mail. When
  the sender's identity is still unknown to you, the message shows an
  **Import the sender's PQ identity** button — after importing, open the
  message again and it decrypts/verifies. Attachments are not encrypted by
  the envelope yet (same as the OpenPGP path).
- **Export** saves the public certificate bundle (never your private keys —
  those stay in the system keyring) into your system download folder as
  `<fingerprint-tail>.pq.pub.pem`; how to inspect and cryptographically
  verify it with OpenSSL is documented in `docs/PQ-OPENSSL-VERIFY.md`.

Delete asks for confirmation and removes the identity together with its keyring
seeds.

---

## 14. Languages

The suite ships in English, German, Spanish, French, Japanese and Chinese. Pick
one in Settings → General; all labels, folder names (Inbox, Sent, …), date names
and CSV headers follow the choice.

---

## 15. Where your data lives

| Data | Location |
|---|---|
| Mail, contacts, tasks and notes database | `~/.local/share/org.gnoppix.calendar/mail.db` |
| Calendar database | `~/.local/share/org.gnoppix.calendar/` |
| Account passwords | OS keyring only (never in the database) |
| Downloaded mail attachments | `~/Download/emails/` (references live in `mail.db`) |
| Voice recordings | `~/.local/share/org.gnoppix.calendar/recordings/` (rows in `mail.db`) |
| Today feed cache | `~/.local/share/org.gnoppix.calendar/feeds.db` — unencrypted by design; only news/forum titles, links and your country preference, never secrets |
| Post-quantum identity backups | `~/.gnoppix-suite/` — `<name>-<fingerprint>.pq.bak`, `.pq.pub.pem`, `.pq.dsa.key.pem`, `.pq.kem.key.pem` and optionally `.pq.pass` (folder 0700, key/pass files 0600; the `.pass` holds your backup passphrase in plain text when you chose to save it) |

If you stop using the suite, remove it with your package manager; your local
databases stay in place unless you delete them.

---

## 16. Troubleshooting

- **Mail syncs nothing but tests pass** — check the incoming server setting; some
  providers need `starttls` (port 143) instead of `imaps` (993). Custom server
  folders are supported; re-run **Sync now** after changes.
- **"Password not stored" error** — your desktop keyring may be locked or absent.
  On GNOME/XFCE unlock the login keyring; on minimal systems install a Secret
  Service provider (e.g. `gnome-keyring`).
- **Encrypted mail won't decrypt** — make sure the OpenPGP tab shows the key your
  sender encrypted to (import it if missing). If that secret key has a
  passphrase, type it when GnuPG's pinentry window appears (once per login) or
  save it in the OpenPGP tab (**Save passphrase**, OS keyring) for automatic
  handling; the message decrypts the next time you open it. A pinentry window
  that pops up during background sync can be cancelled — the body stays
  armored and is retried when you open the message.
- **VPN module says it could not start GnoppixCTL** — install GnoppixCTL
  (`/opt/gnoppixctl/GnoppixCTL`); the module needs `wmctrl` and `xdotool`, which
  the package installs automatically. If its window opens behind other windows,
  press **Bring to front**.
- **Screen reader / accessibility** — accessibility is enabled on systems with a
  working accessibility bus; if WebKitGTK crashes on your system, start with
  `NO_AT_BRIDGE=1 gnoppix-suite`.

---

## 2026-11 update: Mail

- **Drag & drop between folders** — click a message card in any folder, hold the
  left mouse button and drop it on a folder in the left pane; the target folder
  highlights while hovering, a compact sender·subject chip follows the cursor, and
  a "Moved to …" toast confirms. Dropping onto a folder of a different account is
  refused with a notice.
- **Delete goes to Trash** — the Delete button (and the keyboard Delete key) moves
  the selected message into the Trash folder; drag it out of Trash to restore it.
- **Delete advances to the next email** — after deleting the open email (Delete
  button, keyboard Delete key, or right-click menu), the reading pane automatically
  opens the next message in the list: the card that took the deleted one's place,
  or the previous card if the deleted one was at the end. Deleting a card that is
  not the open email leaves the open email open.
- **View Source** — button in the reading pane. It opens the complete original
  message: every header as stored on the mail server (Return-Path, full Received
  chain, DKIM/ARC seals …) plus the raw body. For older messages the first click
  pulls the full copy from the server once, so later opens are instant. If the
  message is no longer on the server (or is a local draft), the header block is
  rebuilt from stored fields and clearly labeled as reconstructed.
  Click again ("Close source") to return to the normal view.
- **Automatic decryption in the background** — encrypted (armored) messages
  decrypt themselves shortly after login; no per-message click needed. If a
  GnuPG passphrase window (pinentry) appears, answer it once — or save the
  passphrase under Settings → OpenPGP — and the rest resolve automatically.
- **Settings → encrypt databases (mail, calendar)** — one switch wraps every
  app database file (`mail.db`, `calendar.db`) in SQLCipher AES encryption;
  each key lives only in the OS keyring. People and Tasks are stored inside
  `mail.db`, so they are covered too. Turn it off the same way to go back to
  plain database files.
- **Settings → Backup NOW** — one click snapshots every database (mail,
  calendar, …) into dated copies named `mail.db-2026-11-03-112205`-style in
  `…/org.gnoppix.calendar/backups/`, safe to run while the app is open. Each
  snapshot keeps its database's form: encrypted databases come back as
  encrypted backups, plain ones stay plain.
- **"Encrypted" indicator is now green** in the message list and reading pane.
