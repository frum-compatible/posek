# PR-01 — actual sources and retrieval limits

Research performed 2026-10-02. Read the requested skill and its routed `references/source-method.md` only. No benchmark, evaluation, expected-answer, or other candidate files were read. No tests/gates or external writes were performed.

## Inspected primary publication

- Rabbi Doniel Yehudah Neustadt, “Moving an Electric Lamp on Shabbos,” OU Torah / Ohr Olam Mishnah Berurah: https://outorah.org/p/49935/. Found through web search and opened as the full article. Inspected all three discussion paragraphs and footnotes i–v. Role: named-author ruling; hand/elbow distinction, plug condition, detached cylinder, reported disagreement. Article appears under the author's name, courtesy of Ohr Olam Mishnah Berurah. No separate print edition was authenticated.
- Its footnote ii cites Igros Moshe, Orach Chaim IV 91:5 and V 23; footnote iii also cites V 22:36. These were read as Neustadt's citations, not independently retrieved responsa. No attempt to reconcile those responsa beyond his stated presentation.
- Its footnote iv cites Mishnah Berurah 308:13, 309:14, 311:30; Beiur Halachah 266:13; Igros Moshe V 22:6; Minchas Shlomo I 14:2. Only the Mishnah Berurah segments identified below were independently inspected. Do not represent the rest as independently checked.

## Helper retrievals actually read

The standalone helper was run with `--output` for each record. Original Hebrew and returned English were inspected; HTML markup was removed only for display. Raw JSON records remain in `work/semicha-pilot/private-scratch/PR-01/`, outside the response deliverables.

| Requested canonical locator | Actual record / time UTC | Evidence and role |
| --- | --- | --- |
| Shulchan Arukh, Orach Chayim 311:8 | SA-311-8.json; 20:44:23 | Mechaber's bodily-movement permission. Read the full se'if, including the radish and straw cases and Rema's separate glosses. The controlling quotation belongs to the Mechaber. |
| Shulchan Arukh, Orach Chayim 279:1 | SA-279-1.json; 20:44:24 | Classical lamp muktzeh rule, even after extinguishing. Modern electric application is attributed to Neustadt, not directly to this se'if. |
| Shulchan Arukh, Orach Chayim 279:2 | SA-279-2.json; 20:44:54 | Neighboring scope: use of object/place does not permit ordinary movement. Read Rema's separate distaste/night-pan gloss; did not apply it to mere light disturbance. |
| Shulchan Arukh, Orach Chayim 308:3 | SA-308-3.json; 20:44:57 | Background definition and movement allowances for kli shemelachto le'issur. Read but not necessary to final citation chain. |
| Mishnah Berurah 308:13 | MB-308-13.json; 20:44:25 | **Numbering mismatch:** API canonical ref is 308:13 but Hebrew starts subsection (יב), concerning availability of a permitted utensil. Not used as evidence for bodily movement. |
| Mishnah Berurah 308:14 | MB-308-14.json; 20:44:55 | Hebrew begins (יג), matching Neustadt's printed subsection 13; includes bodily movement and pushing with the feet. Read to resolve offset, but omitted from final answer to avoid a misleading digital locator. |
| Mishnah Berurah 311:30 | MB-311-30.json; 20:44:56 | Hebrew begins (ל), matching locator. Explains body/other limbs instead of hand and the distinction from other indirect movement. Direct supporting commentary used in answer. |

Shulchan Arukh Hebrew edition returned: *Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893*, Public Domain; English: *Sefaria Community Translation*, CC0. Mishnah Berurah Hebrew edition: *On Your Way*, source http://mobile.tora.ws/, Public Domain. The helper returned no English for the Mishnah Berurah segments; Hebrew was read directly. The answer's short Hebrew translation is my own.

## Failures and limits

- No HTTP/network failure occurred in these retrievals.
- Mishnah Berurah English was unavailable for all three requests, explicitly reported by the helper.
- The Mishnah Berurah 308 digital segment/subsection discrepancy is documented above, not silently treated as a matching citation.
- The unplugging prohibition is explicitly in Neustadt's published text. The explanation that a muktzeh movement permission does not authorize extinguishing is the answer's application of that boundary; no claim about the precise biblical/rabbinic classification of incandescent extinguishing is made.
- The search also returned secondary pages and other articles. They were not used as substantive evidence. No independent review of every authority listed in Neustadt's article was performed.
- Decisive final claims and the Hebrew quotation were checked against the displayed source text before saving.
