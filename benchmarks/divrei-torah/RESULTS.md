# Divrei Torah: initial examples and review

Four fresh candidate sessions used the new divrei Torah workflow on 2026-10-02 UTC. Each received one request and the frozen skill, with the editorial criteria withheld. The finished answers and source records are saved unchanged.

The recorded sessions predate the later hashkafah profiles, audience presets, and institutional persona. Their outcomes do not validate those additions; the input manifest records the revision boundary.

## Read the actual pieces

| Request | Saved output | What it develops |
| --- | --- | --- |
| Yaakov’s pachim ketanim | [Dvar Torah](runs/initial/DT-001.md) | The Gemara explains care for property through refusal of gezel. The piece develops that distinction, considers Yaakov’s large gift to Esav, and retains the nearby warning about danger. |
| Avos and Rambam on lishmah | [Dvar Torah](runs/initial/DT-002.md) | The relationship between serving for truth, receiving reward, and deliberately teaching a learner toward avodah me’ahavah. |
| A wedding vort with an unverified attribution | [Response and vort](runs/initial/DT-006.md) | The requested sefer/page is not invented. A source-based discussion of speech and shalom supports a clearly identified contemporary application. |
| Improve a thin draft for teenagers | [Revised vort](runs/initial/DT-009.md) | The verified Gemara about saying little and doing much replaces an unverified Chazal attribution. A concrete school example develops the kindness theme. |

These examples include both development of familiar teachings and suggested applications. They are not claims of unprecedented chiddushim.

## What was evaluated

A separate AI reviewer checked primary text and assessed source attribution, the source-to-argument connection, the payoff, and audience and length fit. Read the [case-by-case review](runs/initial/REVIEW.md) for factual findings and concrete editorial weaknesses, and the [structured records](runs/initial/review.json) for response hashes and word counts. The review does not turn editorial judgment into an accuracy percentage.

The original [ten-case suite](cases.json) also includes manufactured kushyos, forced source connections, erased disagreement, false attribution of a chiddush, inflated conclusions, and turning a homiletic thought into a heter. Six cases remain unrun: DT-003, DT-004, DT-005, DT-007, DT-008, and DT-010.

The source helper was exercised on live exact segments of Tanach, Rashi, Mishnah, Gemara, and Rambam. Individual candidate source records preserve the references, editions, and available retrieval evidence. Third-party source corpora remain outside the distributed repository; the pieces use brief quotations and independently written explanations.

## Limits

- Four preselected development cases, one fresh session each. No repetitions, randomized review, or no-skill baseline were run for this mode.
- Candidate generation was separated from the rubric. The reviewer knew which workflow was being evaluated, so editorial review was not blinded.
- Exact model identifiers and generation settings were not exposed. The [input manifest](runs/initial/input-manifest.json) records the skill files and their hashes.
- Both the criteria and the review are AI-produced. Primary-source inspection does not replace qualified human Torah or editorial review.
- A saved source log documents the reported retrievals; it is not an immutable export of every tool event. Failure to locate a quotation does not prove it was never said.
- The separate [psak pilot](../RESULTS.md) used an earlier skill revision and does not measure this mode. This pilot does not establish superiority, general halachic reliability, or performance on unseen requests.

The development outputs show how the skill handles composition, revision, and uncertain attribution. They also make its remaining editorial weaknesses available for inspection. Software gates remain on GitHub CI and have not been run locally.
