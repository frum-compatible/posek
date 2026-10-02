# R01 source and retrieval notes

Research began with the supplied skill and its source-method reference at 2026-10-02 20:17:36 UTC. Only that skill tree and the shared retrieval helper were consulted locally; no other candidates, grading material, or project/evaluation files were read. No gates/tests or external writes were performed.

Primary Hebrew inspected:

- Chullin 104a:2–8 (especially Rav Ashi at 7), 104b:11–13, 113a:16–19, 115b:6, 116a:9–16. Sefaria v3 source responses identify William Davidson Edition – Vocalized Aramaic.
- Tosafot Chullin 104b:12:1, s.v. עוף וגבינה אין; 113a:18:1, s.v. בשר בהמה טהורה. Vilna Edition. First located in the Wikisource daf; complete relevant commentary then inspected from Sefaria. The exact 104b segment also has a helper evidence record.
- Rosh on Chullin 8:51, first paragraph. Vilna Edition. This verifies Rosh’s presentation of Rif; Rif was not independently fetched.
- Rambam, Forbidden Foods 9:4, 26, 27, 28. Helper records: Torat Emet 363 Hebrew. English Touger/Moznaim versions were returned, but the answer paraphrases Hebrew and does not reproduce that translation.
- Maggid Mishneh on Forbidden Foods 9:4. ToratEmet. Read the entire paragraph, including its rejected counterargument.
- Beit Yosef YD 89, opening comment (Sefaria chapter response, Tur Yoreh Deah, Vilna, 1923). Read its comparison of Rambam, Ramban, Ran, Rosh, and Rashba. Those underlying original works were not independently inspected for this comparison. Also read the relevant Beit Yosef YD 87 discussion on Wikisource as background.
- Shulchan Arukh YD 87:3, 87:6, 89:1–2, 122:1–2. Sefaria Hebrew: Ashlei Ravrevei, Lemberg 1888. The Mechaber and Rema were distinguished. Whole 87 also browsed on Wikisource.
- Shach YD 87:4 and 87:7 from Sefaria; 87:2–4 additionally visible on Wikisource. 87:4 is decisive for avoiding overstating Tosafot’s suggested explanation. 87:7 was checked for background and not relied on as a separate final ruling.
- Pitchei Teshuvah YD 87:8. Ashlei Ravrevei, Lemberg 1888. Read both opening permission and subsequent מ״מ יש להחמיר. Chamudei Daniel §18 was not directly retrieved. Initial API requests used the accepted alias “Pithei Teshuva”; the returned canonical title is “Pitchei Teshuva.” The corrected exact helper request succeeded.
- Kitzur Shulchan Arukh Yalkut Yosef, Torat Emet page f_01355_part_41.html, 5767 edition, YD 87 paragraph 30. Inspected the full relevant paragraph, including the explicit distinction for Jewish consumption. It cites Issur VeHeter III p. 191, Kol Torah Tammuz 5763 p. 23, and Halichot Olam VII pp. 12, 19; these underlying works were not independently retrieved. Final answer cites only the inspected Yalkut Yosef paragraph and identifies its own cited page.

Retrieval method and failures:

- Used web search only for source discovery; snippets were not treated as final proof. Primary text was inspected through web openings and Sefaria v3 API source responses. The helper was used for several exact segments; other chapter/commentary requests used the same documented v3 endpoint with version=source and fill_in_missing_segments=0. These latter raw responses are retrieval records, not the helper’s validated evidence format.
- Initial helper request with a curly apostrophe in `Yoreh De’ah 87:3` returned HTTP 404. Retried with canonical straight apostrophe; succeeded.
- Web openings of Wikisource’s Pitchei Teshuvah 87 page returned “Internal Error” twice. Sefaria retrieval succeeded.
- An over-specific helper request for `Pitchei Teshuva ... 87:8:1` returned “Response exceeded 2 MiB; use one exact segment reference.” Corrected to `87:8`, which succeeded. No conclusion relies on the failed response.
- The Yalkut Yosef HTML fetched successfully but failed initial UTF-8 decoding. The response’s declared encoding is windows-1255; reading the saved bytes as cp1255 succeeded. The full relevant paragraph was then inspected locally.
- Some combined tool outputs were truncated, so the decisive Pitchei Teshuvah, Shach, Yalkut Yosef, Rambam, and Tosafot passages were inspected separately from saved responses or through focused retrievals.

Raw API/HTML responses and helper evidence records are confined to `private-R01/` under this responses directory. The public answer contains links, short Hebrew quotations, and original English paraphrases; it does not bundle raw editions or translations. The answer’s source-specific qualifications distinguish inspected text, reports through another authority, and uninspected originals.
