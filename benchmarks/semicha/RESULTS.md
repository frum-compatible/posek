# Semicha-question pilot: results

**With Posek instructions: 46/48 review points. Without Posek instructions: 48/48.** Both met this project's pass rule on all four questions. Posek earned full points on three questions and lost two points for omitting one requested explanation on the fourth.

“Without Posek instructions” means the general AI assistant received the same questions and source access, but did not load the Posek skill. It included the explanation Posek missed. This run does not show an accuracy improvement from adding Posek, and no rabbi was evaluated.

Eight fresh candidate sessions answered four adapted public items on 2026-10-02. The [protocol](PROTOCOL.md) and [input manifest](input-manifest.json) record the selection, frozen skill, tools, and review method. These are AI-reviewed development scores, not an official semicha grade or a percentage of halachic accuracy.

[Read the questions and answers](QUESTIONS.md) alongside the original sources and individual reviews.

## What was tested

| Question | With Posek instructions | Without Posek instructions | What the source review found |
| --- | ---: | ---: | --- |
| CR-01 | 12/12 | 12/12 | Both cover the requested positions, interpretations, and practical qualifications. [Review](review/CR-01.md). |
| CR-02 | 10/12 | 12/12 | Posek omits a specifically requested Rema rationale; the baseline includes it. [Review](review/CR-02.md). |
| CR-03 | 12/12 | 12/12 | Both preserve the requested explanations and controlling distinctions. [Review](review/CR-03.md). |
| WY-01 | 12/12 | 12/12 | Both distinguish ordinary validity from a documented preference. [Review](review/WY-01.md). |

No critical failure was found under this rubric. The pilot used three selected questions from one examination paper and one announced course question. [Question provenance](questions.json) identifies the two institutional sources. No authenticated public YU/RIETS examination paper was found in the bounded search; no YU result is claimed.

## The omission that changed the skill

In CR-02, the initial Posek response gives the principal rulings and Shach's two resolutions, but leaves out the separately requested Darkhei Moshe explanation of the Rema's condition. The reviewer deducted one point for conclusion completeness and one for usefulness. A correct final rule did not answer every part of the question.

The source check identified the omitted argument in [Darkhei Moshe, Yoreh De'ah 87:8:1](https://www.sefaria.org/Darkhei_Moshe%2C_Yoreh_De%27ah.87.8.1): the combination of clear and curdled contents matters to the coagulant analysis. Read the review for the full explanation and its sources.

The next skill revision adds a generic check for every requested comparison, named authority, and explanation. This change followed the initial review. Any repeat of CR-02 is a development rerun after feedback and must remain separate from the initial comparison; it cannot establish performance on unseen questions.

The [recorded development rerun](development/RESULTS.md) scored 11/12. It supplies the missing rationale but misnames an adjacent Tosafot heading. That result does not replace the initial 10/12 or change the table above.

## Inspect or reproduce the aggregation

- [Posek judgments](runs/posek/judgments.json) and [generated report](runs/posek/report.json).
- [Baseline judgments](runs/baseline/judgments.json) and [generated report](runs/baseline/report.json).
- Each judgment links an unchanged answer; its adjacent source record lists inspected texts, mediated attributions, and retrieval failures. The input manifest maps opaque review IDs to the saved answers.

From the repository root, regenerate a report from the saved judgments:

```sh
python3 benchmarks/score.py benchmarks/semicha/runs/posek/judgments.json \
  --cases benchmarks/semicha/questions.json --output work/semicha-report.json
```

Create the `work/` directory first if it does not exist. This reproduces the aggregation and response-hash checks, not the model generation or the reviewer's interpretation. GitHub CI checks the saved reports for consistency.

## Limits

- Four selected public items, one answer per condition per item. No human candidates, repetitions, or population-score distribution. No percentile, official exam pass, ordination, or superiority to rabbonim follows.
- Questions were condensed into English, and source access was allowed. This does not reproduce the original institutions' examination conditions. Public questions may have appeared in model training.
- Exact model identifiers and generation settings were not exposed. Both conditions inherited the runtime without overrides, but this is not a reproducible controlled model comparison.
- Three independent AI review sessions assessed opaque response IDs. Style could reveal the condition. Reviewers used digital primary-text transcriptions; there was no qualified human examiner, official marking scheme, or printed-edition collation.
- Candidate source logs are retrospective notes, not immutable exports of every tool event. Independent reviewers checked the substantive sources but did not audit those logs before grading.
- The 10/12 pass threshold is this project's development rule. A passing answer may still omit a requested explanation, as CR-02 demonstrates. Inspect the findings alongside the score.

The [proposed human comparison](../RABBI-COMPARISON.md) describes what a study of practicing rabbonim would require. [Related work](../RELATED-WORK.md) records earlier halachic AI evaluation efforts.
