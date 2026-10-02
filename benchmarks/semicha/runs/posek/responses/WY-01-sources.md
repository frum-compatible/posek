# R07 source and retrieval notes

Question: WY-01. Research began 2026-10-02 at 20:34 UTC; answer drafted by 20:39:30 UTC. Only the supplied skill-v2 Posek SKILL.md and its routed references/source-method.md were read. No other candidate responses, evaluation files, keys or project material were consulted.

## Evidence actually inspected

- Shulchan Arukh, Orach Chayim 647:1 and 647:2: retrieved successfully with supplied fetch_source.py; read Hebrew and returned English. Hebrew edition: Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893. English: Sefaria Community Translation. 647:1 supports species-based validity regardless of desert/mountain location; the controlling sentence belongs to the Mechaber, not the gloss about green stems. 647:2 supplies branch-condition purchasing considerations.
- Mishnah Berurah 647:3 and 647:11: helper succeeded; Hebrew edition On Your Way. No English returned; explicitly warned by helper. Read Hebrew directly. 647:3 reports a better-initially view and Taz's no-need-to-be-particular view; it does not state universal agreement. 647:11 discusses preferring intact foliage.
- Rambam, Mishneh Torah, Shofar, Sukkah and Lulav 7:3: helper succeeded. Hebrew Torat Emet 363 and Eliyahu Touger translation returned and read. Species rather than individual growing location. Answer paraphrases the Hebrew.
- Turei Zahav on Shulchan Arukh, Orach Chayim 647:2: helper succeeded. Hebrew Maginei Eretz, Lemberg 1893; no English (warning recorded). Hebrew independently read, also visible on Wikisource. Supports demonstrating permissibility by using non-river-grown aravos.
- Sukkah 33b: Wikisource primary text page inspected for Mishnah, relevant baraisa and Rashi s.v. ושל בעל, בעל, and ערבי נחל הגדילות על הנחל. Establishes field/mountain validity and Rashi's preference; distinguishes rain-fed ba'al from artificial irrigation.
- Sukkah 34a: Wikisource primary text page inspected for continuation of sugya and Tosafos s.v. ורבנן למקדש מנא להו. Explains competing derashos and stringent river requirement.
- Rosh on Sukkah 3:13: full relevant primary passage read via wiki.jewishbooks.org.il, including the objection, his teachers' practice, species explanation and Rambam comparison. This site says the page was uploaded automatically; not collated against a scan. Web retrieval preserved privately.
- Tur, Orach Chayim 647: inspected original Tur passage on l'chatchilah/b'dieved and Rosh; also read relevant Beis Yosef and Bach discussion on the page. Wikisource warns that this page was produced by OCR and requires checking. Answer relies on the Tur's explicit report, with supporting direct Rosh/Rambam/MB texts, not a count of authorities.
- Arukh HaShulchan, Orach Chayim 647:5–7: primary Hebrew read on Wikisource. Records practice, discusses the stricter view, and offers valley/level-ground interpretation. Explicitly addresses beis hashelachin watered by a person. Did not misattribute his proposal as universally accepted.
- R. Yosef Yona, זני ערבות ודין ערבה שאינה גדלה על הנחל ועוד, HaOtzar issue 57, Tishrei 5782, https://www.ha-otzar.net/article/812: author and issue metadata read on page. Read section ה and subsection ערבות הגדלות על השקיה מלאכותית אם דינן כגדלות על הנחל. Author's own proposed irrigation analysis is cited as tentative, not consensus or an independently verified ruling of someone he quotes.

All direct links used are in R07.md. The short Shulchan Arukh quotation was checked against the saved Hebrew; its English rendering is mine.

## Retrieval problems and limits

- Initial tool command used python, which was available. No dependency installation.
- Sefaria browser page for Sukkah 33b returned only interface/navigation, no substantive text. Sefaria browser Sukkah 34a returned an inaccessible/internal-error response. Switched to Wikisource and read the text there.
- An initial guessed Wikisource path for Rosh returned an internal error. Search identified the JewishBooks primary page.
- fetch_source.py request Rosh on Sukkah 3:13 failed with: "One exact segment is required; book, chapter, and range references are rejected. The API must supply consistent sections, toSections, textDepth, and isSpanning." This did not count as verification. Used the complete relevant passage on JewishBooks instead.
- An attempt to archive the JewishBooks Rosh page using urllib timed out. This did not erase the successful web-tool reading; its web-tool output was subsequently saved to private-R07/rosh-web-retrieval.json.
- Searches for Bikkurei Yaakov 647:2 produced snippets and secondary references. Its original passage was not obtained and it is not relied on or attributed in the answer.
- Broad searches returned secondary discussions and commercial pages; these were only leads, not the basis of the ruling.
- No print-scan collation, inspection of the seller's actual stock/growing conditions, or exhaustive survey of present-day poskim was performed.

## Private retrieval material

All archived raw material is under private-R07/ beside this note; none is in a public output directory.

Helper JSON files: sa647-1.json, sa647-2.json, mb647-3.json, mb647-11.json, rambam7-3.json, taz647-2.json. These contain actual API metadata, warnings, timestamps and hashes generated by the helper.

HTML archives: sukkah33b.html, sukkah34a.html, aruch-hashulchan647.html, tur647.html, rav-yosef-yona.html. The actual download results and timestamps are recorded in html-retrieval-log.json. Rosh web result: rosh-web-retrieval.json.

No software gates, tests, external writes or other-candidate communications were performed.
