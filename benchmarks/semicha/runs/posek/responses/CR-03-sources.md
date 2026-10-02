# CR-03 source/retrieval notes

Research began 2026-10-02 at approximately 20:18 UTC and was completed within ten minutes. No other evaluation/project files or candidate answers were read. Skill read: supplied skill-v2/posek/SKILL.md and routed references/source-method.md only. No external writes or software gates.

## Inspected evidence

- Shulchan Arukh, Yoreh De'ah 70:1, 70:6, 76:1, 91:5, 105:9: exact-segment helper retrievals succeeded. Hebrew edition metadata: Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888; Public Domain. Raw evidence JSON in _private_R03. Mechaber and Rema separated using the Hebrew gloss markers. Hebrew controls; retrieved English 70:1 appears to invert the timing of poultry-juice expulsion relative to beef-blood expulsion, so it was not adopted.
- Rashi on Chullin 113a:13:1: helper succeeded; Vilna Hebrew text inspected. Controls attribution of active expulsion/no absorption to Rashi.
- Tosafot on Chullin 112b:4:1: helper succeeded; Vilna Hebrew text inspected in full. Contains critique of synchronized expulsion, runoff, anonymous ongoing-juice expulsion, R. Yosef of Orleans' continuity mechanism, and waiting for the upper piece. Read also in Wikisource daf.
- Beit Yosef, YD 70, discussion of כתב הרשבא אסור למלוח בשר עם בשר שכבר נמלח and following paragraph: browser primary text inspected. Reports Ran/Rabbeinu Tam; Ran himself was not independently read. Rabbeinu Tam seven-days permission checked in the following paragraph. Wikisource labels this section OCR needing proofreading; no printed scan comparison performed.
- Bach, YD 70, opening paragraph: browser text inspected; explicitly confirms removal-time nafka mina and Tur's adoption of no-absorption mechanism.
- Turei Zahav on Shulchan Arukh, Yoreh De'ah 70:2 and 76:1: exact helper retrievals succeeded and Hebrew inspected. The first explains meat itself hot through salting; second distinguishes dam be'en from naturally expelled blood and defines netilah.
- Shakh YD 70:44, 76:3–5 and 91:11 read in browser primary pages. 76:4 gives lower-hot and on-fire explanations; 76:5 expressly states Ashkenazic sixty rule despite absent local Rema gloss. 70:44 limits inference from within-shiur wording. 91:11 inspected for the salt-heat timing issue; not comprehensively developed in answer.
- Browser raw response preserving the main primary pages: _private_R03/browser-primary-pages.json. More raw Sefaria discovery responses are also confined to _private_R03.

## Actual failures / retrieval limitations

- First attempted helper argument accidentally contained literal backslash-x27 in Yoreh De'ah; returned HTTP 307 and no evidence. Correct apostrophe invocation succeeded.
- The guessed standalone Wikisource בית_יוסף_על_יורה_דעה_ע URL was inaccessible. Beit Yosef was read within the verified טור_יורה_דעה_ע page instead.
- Sefaria legacy api/texts broad commentary calls returned an empty Hebrew array/coerced first-segment references. These are not evidence of absent commentaries. Broad v3 source calls exposed actual arrays; exact helper retrievals for Rashi/Tosafot then succeeded.
- Helper calls for Siftei Kohen 76:4, 76:5, 70:44 and Beit Yosef 70:1 were rejected for lacking exact segment shape. Did not claim helper verification for those; actual browser readings support cited text.
- Direct urllib attempts to archive six Wikisource pages all returned HTTP 403. Browser retrievals worked; main raw browser response saved separately.
- The answer does not claim independently checked original Rabbeinu Tam/Ran manuscripts, printed editions, or an exhaustive later-authority survey.

## Main verified URLs

- https://he.wikisource.org/wiki/חולין_קיג_א
- https://he.wikisource.org/wiki/חולין_קיב_ב
- https://he.wikisource.org/wiki/טור_יורה_דעה_ע
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_ע_א
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_ע_ו
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_עו_א
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_צא_ה
- https://he.wikisource.org/wiki/שולחן_ערוך_יורה_דעה_קה_ט

