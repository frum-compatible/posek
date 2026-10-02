# R05 retrieval notes

Research began 2026-10-02 at approximately 20:26:33 UTC and the decisive source reading was completed within ten minutes. Used only the supplied skill-v2 Posek SKILL.md and its routed references/source-method.md for task instructions. No other candidate answers, evaluation files, or grading keys were read. No gates/tests or external writes were performed.

## Primary evidence actually inspected

- Helper evidence in r05-private-scratch/: Shulchan Arukh, Yoreh De'ah 87:9, 87:10, 87:11; Siftei Kohen on Shulchan Arukh, Yoreh De'ah 87:25:1, 87:29:1, 87:30:1, 87:31:1; Rashi on Chullin 116b:1:2; Tosafot on Chullin 116b:16:1; Mishneh Torah, Forbidden Foods 9:15. Each successful helper record contains its actual retrieval time, API URL, canonical locator, metadata, raw text and hash.
- SA and Shach Hebrew edition returned: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888; marked Public Domain. Rashi/Tosafot: Vilna Edition, Public Domain. Rambam: Torat Emet 363, Public Domain.
- SA English also returned: Ritual of Judaism, derived from Jean de Pavly & M.A.Neviasky, 1898; license recorded as unknown. It was not used for quotations; its rendering of the sixtyfold denominator as “stomach” is clarified from Shach's Hebrew as the stomach milk. Rambam English Touger edition CC-BY-NC was returned but not relied on or quoted.
- Rashi, Tosafot and all requested Shach segments had no English version; helper explicitly warned of this. Read the Hebrew and supplied original English explanations.
- Web primary pages read: Tur YD 87, its Beit Yosef paragraphs ט–י (including the opening discussion, ומשמע מדברי רבינו and ולענין הלכה); Rif Chullin chapter 8, at the printed 38b marker; Chullin 116b with Rashi and Tosafot; SA YD 87:9 with Taz s.k. 7; SA 87:10 with Shach s.k. 26–33 and Taz. Links are in the answer. Wikisource warns its pages are not proofread; the Tur/Beit Yosef section includes an OCR warning. No claim of checking printed scans.
- Initial broad Sefaria API discovery responses for Shach 87:30, Tosafot 116b, and Rashi 116b are also saved privately. These established actual segment depth/indexes; exact-segment helper requests followed.

## Claim-to-source map

- Three Rishonim: Tur 87; corroboration in Rif 38b, Rambam 9:15, Rashi 116b s.v. הרי זו אסורה, Tosafot 116b s.v. הכי גרסינן ברוב ספרים.
- Mechaber/Rema and scope of clear/coagulated distinction: SA 87:9–10, Taz 87:7, Shach 87:25.
- Apparent contradiction and absorbed meat taste: Beit Yosef 87 ט–י; Shach 87:29.
- Rejection of ordinary nat bar nat and explanation based on pirsha: Shach 87:31.
- Sixtyfold denominator, ma‘amid challenge and proposed resolutions: Shach 87:30, read against SA/Rema 87:10–11. Shach's concluding qualification ודוחק קצת retained.
- References to Rabbeinu Yerucham and earlier responsa were inspected only as quoted in Beit Yosef/Shach, not in those original works independently.

## Retrieval failures and limits

1. Initial helper request used curly apostrophe in “Yoreh De’ah 87:10”; Sefaria HTTP 404. Retried canonical ASCII “Yoreh De'ah” successfully.
2. Initial Shach requests at 87:25, 87:29, 87:30, 87:31 failed the helper's exact-segment validation: the commentary requires a third paragraph component. API metadata confirmed depth 3. Retried all as :1 successfully.
3. Web open of Sefaria Tosafot_on_Chullin.116b returned an internal error. Direct Sefaria API discovery and exact helper retrieval succeeded.
4. Web open of the JewishBooks Shach page initially returned a page, but subsequent requested line navigation timed out (400). Used complete Hebrew on Wikisource and successful exact Sefaria Shach records instead.
5. Attempted private archival downloads of the already-read Wikisource Tur/Beit Yosef and Rif pages via Python urllib both returned HTTP 403. Their text was read via the web tool; no local HTML snapshot was saved. Do not infer successful raw archival for these two pages.
6. Search results included modern summaries; these were not used as substantive authority in the answer.

All saved raw source records are confined to r05-private-scratch/. No source verification was inferred merely from a URL existing.
