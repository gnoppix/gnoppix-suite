# Contributing translations

Thank you for helping make Gnoppix Suite speak your language.

## Editing an existing language

1. Fork this repository and clone it.
2. Open `i18n/<your-lang>.json` in any text editor.
3. Improve the wording of any value. Rules:
   - Do **not** change any key (the text left of the colon).
   - Keep every `{placeholder}` exactly as it appears in `en.json`
     (`{n}`, `{error}`, `{name}`, `{email}`, `{label}`, `{p}`, …).
   - Keep arrays the same length (12 months, 12 short months, 7 weekdays,
     9 CSV headers).
   - Leave proper nouns, protocols and symbols untranslated
     (see README.md “Do not translate”).
4. Verify: `python3 check.py` (no dependencies, prints `PARITY OK` per file).
5. Commit with a short message like `de: improve signature labels` and open a
   pull request. Only your language file should change.

## Adding a new language

1. Copy `i18n/en.json` to `i18n/<code>.json` (`<code>` = ISO 639-1 code,
   e.g. `it`, `pt`, `ru`) and translate every value.
2. A maintainer then registers it in `src/i18n/index.js`
   (`RESOURCES` and `LANGUAGES`) — mention this in the PR and we will wire it
   up; translators don't need to touch code.

## Style tips

- Prefer the wording big desktop apps in your language already use
  (Gmail/Calendar/Contacts equivalents) so users recognize the terms.
- Keep UI labels short (buttons, menus); use full sentences for hints and
  error messages.
- Keep the trailing ellipsis character `…` when the English uses it
  (it marks “in progress”, not three dots).

## What happens next

Maintainers run the app with your language and merge. Missing keys fall back
to English automatically, so partial improvements are always welcome —
you don't have to translate everything in one PR.
