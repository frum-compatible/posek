# R06 source and retrieval notes

The answer was researched from primary Hebrew source transcriptions. No installed domain skill, evaluation files, prior candidate answers, or grading keys were consulted. No software tests or gates were run. Raw source material is confined to `.scratch-R06/`.

## Verified texts

- Ḥullin 113a, Rav Sheshet passage and Rashi s.v. אלא לא שנא; Tosafot s.v. אין מחזיקין דם בבני מעיים. Read on Wikisource; raw HTML saved as `chullin113a.html`.
- Tosafot, Ḥullin 112b, s.v. ודגים רפו קרמייהו ופלטי ועופות קמיטי. Read on Wikisource, then located the correct canonical API segment 112b:4:1. This supports the mechanisms and waiting for the upper piece.
- Rashba, Ḥiddushim, Ḥullin 112b, s.v. דגים ועופות, especially ור״ת ז״ל התיר אפילו לאחר כמה ימים. Read in the Rashba section of Wikisource Ḥullin 112b. This is the primary source actually checked for the attribution to Rabbenu Tam; no original RT work was independently inspected.
- Tur and Beit Yosef YD 70 and 76; SA/Rema 70:1, 70:6, 76:1, 91:5, 105:9; Shakh 70:44 and 76:3–5; Taz 76:1. Hebrew read directly, using both web transcription and the evidence files below where available.
- Rosh material checked only as quoted by Beit Yosef, especially BY 76:2:1. No independent Rosh edition checked.
- The Mechaber’s salting-depth application in the answer is explicitly marked as synthesis of general rules, rather than an invented express droplet ruling at 70:6.

## Exact helper retrievals

These are actual successful helper outputs; each JSON preserves the original text/markup, canonical reference, URL, timestamp, version metadata, hash, and warnings. No metadata was invented.
- `by70-1-1.json` — Beit Yosef, Yoreh De'ah 70:1:1; retrieved 2026-10-02T20:30:05.268889Z. Versions: Tur Yoreh Deah, Vilna, 1923 [he].
- `by76-1.json` — Beit Yosef, Yoreh De'ah 76:1:1; retrieved 2026-10-02T20:30:51.816776Z. Versions: Tur Yoreh Deah, Vilna, 1923 [he].
- `by76-2-1.json` — Beit Yosef, Yoreh De'ah 76:2:1; retrieved 2026-10-02T20:32:08.327529Z. Versions: Tur Yoreh Deah, Vilna, 1923 [he].
- `sa105-9.json` — Shulchan Arukh, Yoreh De'ah 105:9; retrieved 2026-10-02T20:32:07.989452Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he]; Ritual of Judaism. Derived from French translation by Jean de Pavly & M.A.Neviasky, 1898 [en].
- `sa70-1.json` — Shulchan Arukh, Yoreh De'ah 70:1; retrieved 2026-10-02T20:29:06.920715Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he]; Ritual of Judaism. Derived from French translation by Jean de Pavly & M.A.Neviasky, 1898 [en].
- `sa70-6.json` — Shulchan Arukh, Yoreh De'ah 70:6; retrieved 2026-10-02T20:29:33.329695Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he]; Ritual of Judaism. Derived from French translation by Jean de Pavly & M.A.Neviasky, 1898 [en].
- `sa76-1.json` — Shulchan Arukh, Yoreh De'ah 76:1; retrieved 2026-10-02T20:29:33.325401Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he]; Ritual of Judaism. Derived from French translation by Jean de Pavly & M.A.Neviasky, 1898 [en].
- `sa91-5.json` — Shulchan Arukh, Yoreh De'ah 91:5; retrieved 2026-10-02T20:30:51.389287Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he]; Ritual of Judaism. Derived from French translation by Jean de Pavly & M.A.Neviasky, 1898 [en].
- `shach70-44.json` — Siftei Kohen on Shulchan Arukh, Yoreh De'ah 70:44:1; retrieved 2026-10-02T20:30:51.140565Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he].
- `shach76-3.json` — Siftei Kohen on Shulchan Arukh, Yoreh De'ah 76:3:1; retrieved 2026-10-02T20:30:51.449232Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he].
- `shach76-4.json` — Siftei Kohen on Shulchan Arukh, Yoreh De'ah 76:4:1; retrieved 2026-10-02T20:30:51.260436Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he].
- `shach76-5.json` — Siftei Kohen on Shulchan Arukh, Yoreh De'ah 76:5:1; retrieved 2026-10-02T20:30:51.262027Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he].
- `taz76-1.json` — Turei Zahav on Shulchan Arukh, Yoreh De'ah 76:1; retrieved 2026-10-02T20:30:04.813489Z. Versions: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888 [he].
- `tos112b-4-1.json` — Tosafot on Chullin 112b:4:1; retrieved 2026-10-02T20:32:07.985912Z. Versions: Vilna Edition [he].

The English translations, where returned, were not the basis for the answer. Some English text is missing; the helper records that warning. The answer uses Hebrew, particularly where the API English rendering is loose.

## Failed requests and recovery

- Helper request `Shulchan Arukh, Yoreh De’ah 70:1` with a curly apostrophe returned HTTP 404. Retried with straight apostrophe and succeeded.
- Guessed helper reference `Tosafot on Chullin 112b:14:1` returned HTTP 404. Retrieved a broad primary API response only to discover indexing (`tosafot112b-raw.json`), then successfully fetched canonical segment `Tosafot on Chullin 112b:4:1`.
- Helper reference `Beit Yosef, Yoreh De'ah 70:1` failed the one-exact-segment shape check; `70:1:1` succeeded.
- Shakh references `70:44`, `76:3`, `76:4`, `76:5` failed that same exact-segment check; adding the terminal `:1` succeeded for all four.
- Web opens of these guessed titles failed with an internal/inaccessible-page error: `בית יוסף על יורה דעה ע`, `בית יוסף על יו״ד ע`, `תוספות על הש״ס/חולין/פרק ח`, `ש״ך על יורה דעה ע`, `בית יוסף/יורה דעה/עו`. The sources were then read on the Tur, Gemara, or individual Shulchan Arukh סעיף pages.
- The TorahLeshma BY 70 search result appeared, but opening that page failed; it was not relied on for verification.

## Scope limits

No print-edition collation was performed. Wikisource flags some transcriptions as unchecked/OCR; the important BY passages were additionally obtained from the Sefaria API, and the lengthy Tosafot passage was read directly rather than relying solely on BY’s quotation. Rishon attribution evidence is as described above. The response is an exam analysis, not a fact-specific kitchen ruling.

All seven HTML archival requests succeeded; exact URLs and byte counts are in `.scratch-R06/wiki-retrievals.json`. The broad Tosafot API discovery payload is separate from the strict segment evidence.
