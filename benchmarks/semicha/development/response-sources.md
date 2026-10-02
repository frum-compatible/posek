# CR-02 retrieval notes

Research began 2026-10-02 20:48:52 UTC and finished by 20:55:12 UTC (6 minutes 20 seconds). The saved answer was reread and contains 875 whitespace-delimited words. Only the supplied skill-v3 Posek SKILL.md and its routed references/source-method.md were read as task instructions. No other evaluation files, answers, keys, or candidate messages were read.

## Inspected primary texts

- Shulchan Arukh, Yoreh De‘ah 87:9. Successful supplied-helper retrieval at 20:49:28.352712Z; canonical reference matched. Hebrew edition: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888; metadata says Public Domain. Payload SHA-256: 126762d4f70eb76bc81c215d6aaf9385205d09dbaeb8b24c83b9eaaa5580cd3f. Read Hebrew and returned English; final uses original paraphrase, not that translation. Also read https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_פז_ט, including Shach 24–25 and Taz's comment.
- Shulchan Arukh, Yoreh De‘ah 87:10. Successful supplied-helper retrieval at 20:50:01.052521Z. Same Hebrew edition. Payload SHA-256: 7c984688a767248dd764c9a39516246c38f89dcd8787acd945688ef8c2dcd43b. Raw record saved only to private scratch: ../work/repair-cr02-private/source-0.json. The English has license metadata “unknown”; no English excerpts reproduced. Note that its loose rendering of the ratio must not replace Shach’s precise explanation.
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_פז_י. Read se‘if 10, Shach 26–33 (decisive: 29, 30, 31), and Taz. Full Shach 30 text was available in browser output; the answer is not based merely on the search snippet.
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_פז_יא. Read the Mechaber and Rema on an independently forbidden coagulant, permitted stomach skin, and zeh vezeh gorem.
- https://he.wikisource.org/wiki/טור_יורה_דעה_פז. Read Tur’s closing stomach-milk passage; Beit Yosef section [ט-י], especially the final practical distinction; Beit Yosef [יא]; Darkhei Moshe (ח), including both his flavor-based and mixed-cause explanations. Relevant web output lines: Tur 119; Beit Yosef 150–154; Darkhei Moshe 188–189. These are locations in the retrieved web rendering, not canonical printed line numbers. This is a composite page, and it carries an OCR/proofreading warning.
- https://he.wikisource.org/wiki/רמב%22ם_הלכות_מאכלות_אסורות_ט_טו. Read Rambam, Ma’akhalot Asurot 9:15 directly. Page labels printed text and says no corrected text is supplied.
- https://he.wikisource.org/wiki/חולין_קטז_ב. Read printed Rashi s.v. הרי זו אסורה and Tosafot s.v. כאן לאחר חזרה, including the Rabbeinu Tam passage. Printed Rashi’s long gloss ends with an attribution formula to material found in the notes of R. Shlomo b. Meir; no independent attribution investigation was attempted.
- https://he.wikisource.org/wiki/עבודה_זרה_לה_א was opened successfully, but the returned full contents were not necessary for the answer. No claim rests on having inspected its Tosafot.

## Failures and limited retrievals

1. Initial helper request mistakenly supplied a literal backslash-u0027 in the book title: `Shulchan Arukh, Yoreh De\u0027ah 87:10`. It returned HTTP 307 and explicitly produced no source evidence. Correct apostrophe spelling succeeded subsequently for 87:9 and 87:10.
2. Helper requests for `Siftei Kohen on Shulchan Arukh, Yoreh De'ah 87:29`, `87:30`, and `87:31` each failed the helper’s exact-segment metadata check: “One exact segment is required; book, chapter, and range references are rejected. The API must supply consistent sections, toSections, textDepth, and isSpanning.” No successful Sefaria commentary verification is claimed.
3. Opening https://wiki.jewishbooks.org.il/mediawiki/wiki/דרכי_משה/יורה_דעה/פז timed out. Its search result was only a lead; the complete decisive passage was later read on the Wikisource Tur composite page.
4. Guessed standalone Wikisource pages `בית_יוסף_על_יורה_דעה_פז` and `דרכי_משה_על_יורה_דעה_פז` were inaccessible. Navigation to the actual Tur composite page supplied those texts.
5. TorahLeshma pages for Beit Yosef YD 87 and Darkhei Moshe YD 87 returned internal errors when opened. Their search snippets were not treated as complete verification.
6. Sefaria web pages for Siftei Kohen YD 87:30 and Darkhei Moshe YD 87 returned titles and interface text, without the source bodies. They confirm no substantive text.
7. A direct web-tool attempt to open the Sefaria v3 API for Siftei Kohen YD 87:30 was inaccessible.
8. Supplied-helper request for `Darkhei Moshe, Yoreh De'ah 87:8` failed the same exact-segment metadata check as the Shach requests. No evidence file was produced; final attribution rests on the inspected Wikisource Hebrew.

Search also surfaced later summaries and exam-preparation material. None was opened or used as a halakhic authority. Search was used to locate the primary texts above.

## Scope and attribution controls

- The three opinions are compared as reported in Tur and supported by direct Rambam, printed Rashi, and Tosafot readings. Rif himself was not independently read.
- The two levels of Shach’s reconciliation are kept distinct from his preliminary suggestion about Tur/Rabbeinu Tam, and from Rema’s own Darkhei Moshe argument.
- The Mechaber’s b’dieved position is identified through Beit Yosef and Shach; it is not falsely presented as explicit wording in the short Shulchan Arukh se‘if.
- Rabbeinu Barukh/Mordekhai and other authorities quoted by Shach were not independently retrieved.
- No practical certification, exhaustive later-authority survey, manuscript comparison, tests, local gates, or external writes were performed. Only the requested response files and private retrieval scratch were written.
