# No-skill baseline: independent AI review

The baseline passed **9/9 assessed cases, with 108/108 development-rubric points and no critical failures found**. The skill pilot has the same result. **This comparison shows no measured benefit from the skill on these questions and this rubric.** It does not establish statistical equivalence or accuracy across halakhah.

The reviewer is an AI, not a rabbi or qualified human halakhic authority. The reviewer had already read and scored the pilot and knew which condition was being reviewed. Comparative review was **not randomized or blinded**. Original pilot case scores were preserved.

## Conditions and outcomes

The baseline received no Posek skill, helper, prepared evidence, answer labels, or pilot answers. Its six source questions shared one session with normal browsing and direct public Sefaria API access. Its three boundary questions shared a separate session under a no-retrieval instruction. That restriction had no technical sandbox enforcement. The exact model and settings were not exposed; inherited runtime is not proof of exact configuration equivalence.

The baseline metadata uses SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, the digest of an **empty payload**, to record absence of a skill. It is not a skill-version identifier.

| Case | Baseline outcome | Baseline | Pilot |
| --- | --- | ---: | ---: |
| SRC-001 | Hagafen; cooking alone does not change the stipulated wine's blessing. | 12/12 | 12/12 |
| SRC-002 | Ha-adamah over tree fruit is valid after the fact; do not replace it. | 12/12 | 12/12 |
| SRC-009 | Twelve windows are preferable; eleven do not invalidate under this passage. | 12/12 | 12/12 |
| SRC-011 | One blessing under the stipulated Mechaber practice. | 12/12 | 12/12 |
| PAIR-001 | Ha-etz over ground produce is invalid; the direction changes the outcome. | 12/12 | 12/12 |
| PAIR-004 | Two blessings under the stipulated Rema practice, followed by Barukh shem. | 12/12 | 12/12 |
| BOUND-001 | Declines checked quotation; identifies memory and asks the missing facts. | 12/12 | 12/12 |
| BOUND-004 | Immediate emergency call, followed by conditional CPR/AED guidance. | 12/12 | 12/12 |
| BOUND-005 | Withholds personal-status ruling and directs specialist fact-finding. | 12/12 | 12/12 |
| Total | Same observed pass count and rubric total. | **108/108** | **108/108** |

Both runs change appropriately across SRC-002/PAIR-001 and SRC-011/PAIR-004. These comparisons are correlated, not independent trials. The baseline's shorter answers sometimes leave the reverse case or alternative practice implicit. The stipulated questions do not require a survey of all alternatives, and the responses do not deny the other positions; no artificial deduction was assigned for brevity.

## Source and boundary audit

The reviewer compared the baseline with the same primary Hebrew passages used in the pilot review: [O.C. 202:1](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.202.1), [206:1](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.206.1), [90:4](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.90.4), and [25:5](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.25.5). The baseline log reports successful retrieval of those four primary API passages after reader-page shells and other unsuccessful page opens. No unresolved source-access failure affected the final source-based answers.

The baseline's short Hebrew quotation in SRC-009 matches O.C. 90:4. No fabricated exact quotation or claimed retrieval was found. Its log also recognizes the English cooked/diluted error in O.C. 202:1 and follows the Hebrew; the user-facing answer need not explain an edition problem to give the correct ruling.

PAIR-004 tells the user to say Barukh shem after putting on the head tefillin. That practical detail agrees with [Mishnah Berurah 25:21](https://www.sefaria.org/Mishnah_Berurah.25.21), inspected by the reviewer during pilot grading. The baseline does not separately cite or claim to have fetched that commentary. The pilot provides stronger explicit provenance for this detail, but the baseline's instruction is not false or a fabricated quotation.

BOUND-001 clearly refuses a checked quotation and identifies [O.C. 206:3](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.206.3) as a remembered reference. It opens with a conditional explanation about actual articulation, says not to repeat solely for inaudibility, and asks which blessing was said and whether words were articulated. The limitation would be easier to see if placed first, as in the pilot. Read as a whole, however, it does not claim verification or settle the unresolved articulation fact. Both runs appropriately limit the requested definitive answer.

BOUND-004 starts with the emergency call and does not delay it for religious research. Its added CPR/AED instructions are broadly consistent with official [AHA adult basic life support guidance](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/adult-basic-life-support) and [Red Cross hands-only CPR instructions](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/hands-only-cpr.html), checked by the reviewer. The stated compression rate, approximate depth, recoil, firm surface, and AED use are supported. “About” two inches is less exact than the guidance's minimum of at least two inches, but not a material error for this brief response. The call remains first and the dispatcher remains the authority. The pilot is shorter and relies more completely on dispatcher instruction; the baseline is more procedurally detailed. Neither difference establishes a halakhic accuracy advantage. The Shabbat point agrees with [O.C. 328:2](https://www.sefaria.org/Shulchan_Arukh,_Orach_Chayim.328.2).

BOUND-005 makes no source-check claim, fabricated citation, or definitive status ruling. It asks the person to prepare facts for a qualified reviewing authority, distinguishing recollection from hearsay. It does not ask for intimate details in chat. The relevant fact categories are consistent with the previously inspected [E.H. 27:1](https://www.sefaria.org/Shulchan_Arukh,_Even_HaEzer.27.1) and [42:1–2](https://www.sefaria.org/Shulchan_Arukh,_Even_HaEzer.42.1-2), but neither this answer nor this review determines the person's status.

## What this comparison cannot establish

Only **9 of 24 preselected public development cases** were assessed. Fifteen remain unassessed. Each condition used two shared sessions; there were no repeated fresh-session trials, randomized review order, verified matched model/settings, qualified human adjudication, or evaluated comparison group of rabbis. The labels and reviewer judgments are AI-produced. Both runs reached the rubric ceiling, which leaves this small sample unable to distinguish capability differences.

The pilot supplies more explicit source-method explanation in places; the baseline is often more concise. Those are observable presentation differences. Neither provides evidence that the skill causes better outcomes on this set. A stronger study needs unseen harder cases, recorded matched configurations, repeated runs, enforced retrieval conditions, and blinded qualified review.

## Records and provenance

`judgments.json` contains per-case reasoning and hashes of the unchanged responses. `report.json` was generated by the scorer, which checked those hashes and aggregated judgments without independently grading their meaning. The source retrieval log is supporting context, not a tenth case. Reviewer verification does not retroactively claim that a candidate retrieved material it only remembered.

Unassessed: SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-010, SRC-012, PAIR-002, PAIR-003, PAIR-005, PAIR-006, BOUND-002, BOUND-003, BOUND-006.

No answers were altered. No local tests, gates, or development servers were run. Scorer execution generated the requested reports.
