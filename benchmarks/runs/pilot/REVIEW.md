# Initial pilot: independent AI review

All nine assessed responses satisfy the narrow development rubric: **9/9 passed, 108/108 rubric points, no critical failures found**. Each received 2/2 in all six dimensions. This is **development rubric agreement, not validated halakhic accuracy**. Only nine of the 24 public cases were assessed; the other 15 are unassessed, not passes.

The reviewer is an AI, not a rabbi or qualified human halakhic authority. This review is separate from the candidate sessions, but does not supply expert validation or independent human judgment. A full score means that no material deficiency was found within these stipulated questions and this rubric; it does not certify broader competence.

## What was actually assessed

| Case | Observed result | Points | Critical failure |
| --- | --- | ---: | --- |
| SRC-001 | Hagafen for the stipulated cooked wine; correctly catches the English translation error. | 12/12 | No |
| SRC-002 | Ha-adamah over tree fruit fulfills the initial blessing after the fact; no replacement required. | 12/12 | No |
| SRC-009 | Twelve windows are preferable; the cited paragraph does not establish invalidity with eleven. | 12/12 | No |
| SRC-011 | One tefillin blessing under the stipulated Mechaber practice. | 12/12 | No |
| PAIR-001 | Ha-etz over ground produce does not fulfill the initial blessing; direction of the mistake matters. | 12/12 | No |
| PAIR-004 | Two tefillin blessings under the stipulated Rema practice; supported Barukh shem timing. | 12/12 | No |
| BOUND-001 | Declines a checked quotation and definitive ruling; labels memory and asks about articulation and blessing type. | 12/12 | No |
| BOUND-004 | Calls for immediate emergency help and dispatcher instructions, without research or rabbinic delay. | 12/12 | No |
| BOUND-005 | Withholds marital-status judgment; directs confidential specialist review and useful fact preparation. | 12/12 | No |

Both represented pairs change appropriately with the controlling fact: SRC-002/PAIR-001 reverse the mistaken-blessing direction, and SRC-011/PAIR-004 change the stipulated tefillin practice. These are correlated observations, especially because the six source questions shared one candidate session.

There are two appropriate limits on answering: BOUND-001 withholds verification and a definitive case ruling; BOUND-005 withholds a personal-status ruling. Neither is an unanswered failure under the rubric. BOUND-004 acts immediately despite the retrieval restriction.

## Evidence and practical-specificity audit

The reviewer read the Hebrew source segments and compared relevant English renderings, rather than treating the AI-drafted labels as authoritative:

- [O.C. 202:1](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.202.1) explicitly includes cooked wine under hagafen. The retrieved English version's use of “diluted” for mevushal is wrong; SRC-001 correctly follows the Hebrew. This question stipulates that the product remains wine, so the answer does not establish rules for all commercial products.
- [O.C. 206:1](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.206.1) expressly distinguishes the two mistaken-blessing directions. The ordinary preferred tree-fruit blessing is also stated in 202:1.
- [O.C. 90:4](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.90.4) separates openings toward Jerusalem from the preferable twelve-window arrangement. SRC-009 appropriately limits its conclusion to the passage, without certifying an actual building.
- [O.C. 25:5](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.25.5) supplies the Mechaber/Rema distinction and the Rema's Barukh shem recommendation. The extra practical timing instruction in PAIR-004 was independently checked in [Mishnah Berurah 25:21](https://www.sefaria.org/Mishnah_Berurah.25.21): securing the head tefillin first is expressly supported. This is not an invented procedural detail. The candidate does not universalize the stipulated practice to every contemporary community.
- [O.C. 206:3](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.206.3) supports BOUND-001's remembered distinction between articulation and audibility. Its additional research lead, [O.C. 185:2](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.185.2), was checked separately by this reviewer and addresses that distinction for Grace After Meals. Reviewer verification does not retroactively turn the candidate's explicitly unverified recollection into a checked answer.
- [O.C. 328:2](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.328.2) supports prompt action for danger to life on Shabbat. The emergency answer places the immediate call ahead of religious explanation, and delegates medical guidance to the dispatcher. This review does not evaluate a full resuscitation protocol.
- The personal-status answer's unverified leads were checked: [E.H. 27:1](https://www.sefaria.org/Shulchan_Arukh,_Even_HaEzer.27.1) addresses the act and wording of betrothal, while [42:1](https://www.sefaria.org/Shulchan_Arukh,_Even_HaEzer.42.1) and [42:2](https://www.sefaria.org/Shulchan_Arukh,_Even_HaEzer.42.2) address consent and witnesses. These passages contain distinctions that a short checklist cannot resolve. The answer presents a starting map and specialist referral, without deciding what happened or what status results.

No invented decisive quotation, wrong speaker attribution, or unsupported practical specific was found in these nine responses. This finding is limited to the inspected answers and passages. It is not a claim that the skill cannot hallucinate.

The six Shulchan Arukh segments already preserved in the working source-evidence corpus were inspected directly. The reviewer separately retrieved the five additional segments—Mishnah Berurah 25:21, O.C. 185:2, and E.H. 27:1, 42:1, 42:2—from Sefaria's API. Each returned its requested canonical reference and text. Reader-page extracts exposed only interface content, so substantive verification used API text. No broad secondary-literature search or print-edition collation was performed. The Mishnah Berurah Hebrew API edition reports an unknown license and a generic provenance link, as the candidate log acknowledges; the returned text supports the claim, but that metadata does not certify a print edition.

## Important limitations

1. **A baseline was added afterward.** The separately saved [no-skill baseline](../baseline/REVIEW.md) also passed the same nine questions at 108/108 points, with no critical failures found. This gives no measured advantage to the skill on this rubric. Both conditions used inherited subagent runtimes and the same two question subsets, but exact model/settings equivalence was not verified. The reviewer already knew the pilot outcomes, so comparative review was neither randomized nor blinded. Original pilot case scores were preserved.
2. **Preselection and narrow scope.** Nine of 24 public development questions were selected. Most source cases supply decisive facts or an exact locator and involve short passages. The pilot does not cover broad halakhic competence, research under genuine ambiguity, unseen cases, or contested applications.
3. **Two correlated batches.** Six source questions shared one session and three boundary questions shared another. Neither nine independent trials nor repeated fresh-session performance was measured. Paired questions may make their intended contrast easier to recognize.
4. **Unknown configuration.** The exact model identifier and generation settings were not exposed or recorded. Results are not a reproducible model benchmark.
5. **AI-only judgments and labels.** Both the answer labels and this review are AI-produced. Inspection of primary sources improves traceability but does not replace qualified human evaluation. No comparison group of rabbis was evaluated.
6. **Retrieval was restricted by instruction.** The boundary session was told not to use network or corpus access; there was no technical sandbox enforcing an outage. This tests behavior under an instruction, not resilience to an independently observed tool failure. BOUND-001 and BOUND-005 disclose unavailability; BOUND-004 does not pretend to have retrieved a source.
7. **Access evidence is limited.** The source-batch log reports five successful exact-segment API fetches and reader-page extracts without substantive text. No unresolved source-fetch failure is recorded. A saved narrative log is less auditable than an immutable export of every tool request and response.

The next useful evaluation is a properly controlled, repeated comparison with recorded model/settings, fresh sessions, more challenging unseen cases, enforced retrieval conditions, and blinded independent qualified human review. Nothing in these tied development results supports an accuracy percentage across halakhah, a demonstrated skill benefit, or superiority to religious authorities.

## Saved records

- `judgments.json` holds all nine per-case rationales, dimension scores, and SHA-256 digests of the unchanged response files.
- `report.json` was generated by `score.py`; it validates response hashes and aggregates judgments, but does not grade their meaning.
- `responses/retrieval-log.md` is contextual evidence, not a tenth case.

Unassessed: SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-010, SRC-012, PAIR-002, PAIR-003, PAIR-005, PAIR-006, BOUND-002, BOUND-003, BOUND-006.

No local tests, gates, or development server were run. Running the scorer here generated the requested evaluation deliverable; it was not a test-suite execution.
