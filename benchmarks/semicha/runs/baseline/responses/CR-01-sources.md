# R04 retrieval notes

Question: CR-01. Research began at 2026-10-02 20:24:13 UTC; last source retrieval completed by 20:31:44 UTC (under eight minutes). No installed domain skills, other candidates, earlier answers, evaluation files, or grading keys were used. The only pre-existing local file read was the authorized standalone `tools/fetch_source.py`. No software gates were run. All writes were local.

## Sources actually inspected

The answer is based on Hebrew text. Sefaria English versions were sometimes returned but their explanatory footnotes were not treated as words of the original author.

- Gemara: Chullin 104a (especially 7), 104b (11–13), 113a (18–19), 115b (6), and 116a (13–14). Full-daf legacy API responses were used to locate segments, then key segments were retrieved with the strict helper. The helper successfully returned 104a:7, 104b:11–12, 113a:18, 115b:6, and 116a:13.
- Tosafot, Chullin 104b:12:1, ד״ה עוף וגבינה אין בשר וגבינה לא; 113a:18:1, ד״ה בשר בהמה טהורה. Both Hebrew passages read through Wikisource and then successfully retrieved by the strict helper.
- Rosh, Chullin 8:51:1: successfully retrieved with the helper; also read in the Wikisource chapter. Rif's position is reported **through Rosh**, not a separately examined Rif edition. Rosh 8:5 was also read in the Wikisource chapter.
- Rambam, Ma’achalot Asurot 9:4, 9:26–28: Hebrew read through the Sefaria APIs. Helper evidence exists for 9:4, 26, 27; 9:28 is in a saved legacy response.
- Maggid Mishneh, Ma’achalot Asurot 9:4:1: strict-helper retrieval, including his interpretation of the Mishnah's cooking language and the objection he discusses.
- Beit Yosef, YD 89:1:1: read in Wikisource's Tur YD 89 page and retrieved with the strict helper. Statements of Ramban, Ran, and Rashba in this answer rely on **Beit Yosef's quotations/report**; no separate edition of those works was collated. Beit Yosef YD 87 was also read within the Tur YD 87 page.
- Shulchan Aruch/Rema: YD 87:3,6; 89:1,2; 103:5; 122:2. All successfully retrieved with the strict helper. YD 87 was also read on Wikisource.
- Shakh YD 87:2,4: read in the Wikisource transcription. Its discussion cautions against presenting Tosafot's explanation of custom as an uncontested final Torah-level ruling. Final browser output saved privately.
- Pitchei Teshuvah YD 87:8: first located in the saved legacy chapter response, then successfully retrieved with the strict helper. The entry includes both the permissive reasoning and `מ״מ יש להחמיר`; Chamudei Daniel §18 itself was **not** independently retrieved.
- Ben Ish Chai, year II, Beha’alotekha §11: the full relevant Hebrew paragraph was read in the [Ashoova transcription](https://ashoova.co.il/ask/בן-איש-חי-הלכות-ב-בהעלותך-י״א/amp/). Final browser output saved privately. It expressly permits the ordinary pot case and restricts visibly distinctive large meat cookware.

## Retrieval failures and limitations

- Web opening standalone Wikisource `בית יוסף על יורה דעה פט` and `...פז` failed. The texts were available embedded in the corresponding Tur pages.
- Sefaria web opening Tosafot 104b:1:1 returned page chrome without the text. Broad web pages for Tosafot 104a/113a were inaccessible. Legacy API broad Tosafot requests silently selected the first comment, which was irrelevant; those responses were not treated as the requested passage. Exact comments above resolved this.
- Initial guesses Chullin 104b:1, 113a:10, 116a:1 and Tosafot 104b:1:1 retrieved valid but irrelevant passages. They were discarded as evidence for the answer; raw responses remain in the private directory.
- Strict helper rejected `Rosh on Chullin 8:51` as non-segment-level; `8:51:1` subsequently succeeded.
- Strict helper request `Ben Ish Hai, Halakhot 2nd Year, Beha'alotcha 11` returned HTTP 400. A guessed Wikisource year-II page also failed. Direct archival download of the successful Ashoova page returned HTTP 403; the browser tool successfully displayed the paragraph and its output was saved instead.
- Some searches produced modern summaries and unrelated hits. They were used only to find primary-text locations, not as authority for the final claims. No printed-page images or manuscripts were checked.

Raw retrieved text and helper evidence are confined to `responses/private-R04/`. Helper JSON preserves the actual returned source/translation text, version metadata, warnings, and retrieval provenance; no missing edition metadata was invented. Legacy API files are locator/transcription records, not helper-certified segment evidence. Final answer: `responses/R04.md`.
