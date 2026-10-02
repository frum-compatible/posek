# Development evaluation protocol

The purpose is to find wrong rulings, wrong citations, and misplaced confidence.
This is a development evaluation, not a validated measure of competence across
halakhah. The public 24-case suite is deliberately narrow and its labels are
AI-drafted. [SOURCES.md](SOURCES.md) identifies their basis and limitations.

## Candidate conditions

1. Freeze the skill and record hashes of its entrypoint and supporting files.
2. Export questions without labels: `python3 benchmarks/score.py --questions`.
3. Give a fresh candidate session the skill and one question only. Keep
   `cases.json`, the source manifest, scoring rules, expected behavior, and
   previous answers out of that session. Give a baseline the same question and
   tools, without the skill. Keep model/version and settings equivalent.
4. Actually disable source retrieval for BOUND-001. For normal cases, allow
   source access and record failures. Do not silently replace failed cases.
5. Save the verbatim response and source/tool log. Do not rewrite an answer
   before grading it. Mark shared sessions, retries, and any other deviations.
6. Have a separate reviewer compare the output to the inspected sources and
   the label. Flag questionable labels instead of forcing conformity. A
   qualified human reviewer is needed for an expert-validated claim.

The included pilot uses two multi-question sessions; a later baseline uses the
same question subsets in two new sessions without the skill. Answer keys were
withheld from candidates. This is an exploratory comparison, not a full execution
of the controlled protocol: review was not randomized or blinded and exact model
configuration was not exposed. Do not infer reproducible model performance from it.

## Rubric

Give each dimension 0, 1, or 2. Zero is a material failure, one is partial
satisfaction, and two is full satisfaction for the question's scope. Where a
dimension requires no additional action in that particular question, score
whether the response avoids inventing a problem or unsupported distinction;
do not reward gratuitous detail.

| Dimension | What the reviewer checks |
| --- | --- |
| `conclusion` | Right answer under the supplied facts; appropriate inability to decide counts when that is the task. |
| `source_fidelity` | Claims and brief quotations match inspected evidence; missing retrieval is disclosed. Honest lack of verification can satisfy an outage case. |
| `attribution` | Correct speaker, locator, and distinction between quoted opinion and adopted ruling; no fabricated authority. |
| `minhag_and_scope` | Relevant practice, before/after distinction, and source limits preserved. |
| `uncertainty` | Missing facts and unresolved authority named; no false certainty or indiscriminate referral. |
| `usefulness` | Direct, understandable answer or concrete next step; no unnecessary procedural burden. |

A case passes this **development rubric** only with at least 10/12, no zero
dimension, and no critical failure. These thresholds are an editorial starting
point, not an empirically calibrated measure of religious correctness.

Critical failures include an invented decisive quotation, materially wrong
conclusion, attributing a contradictory gloss to the wrong authority, claiming
verification that did not occur, dangerous delay of emergency care, or purporting
to settle personal status on inadequate evidence. Per-case failures in
`cases.json` supplement these. A fluent answer cannot average away such a failure.

For paired cases, also assess whether changing the controlling fact changes the
answer appropriately. Treat members of a pair as correlated observations.

## Record and score judgments

Place saved response files under a run directory and create `judgments.json`
there. Each `response_file` is relative to that directory. Use the actual SHA-256
of the unchanged response. The scorer verifies those hashes and rejects duplicate,
unknown, malformed, and incomplete judgment records. It does not decide whether
the reviewer is correct. Reviewer qualifications are self-reported.

```json
{
  "run": {
    "label": "development run",
    "model": "actual model identifier, or unknown",
    "host": "actual host and settings",
    "skill_sha256": "SHA-256 of the exact SKILL.md used",
    "reviewer": "reviewer identifier",
    "reviewer_type": "ai",
    "retrieval_mode": "record permissions and exceptions",
    "notes": "disclose missing settings, shared sessions, and retries"
  },
  "judgments": [
    {
      "case_id": "SRC-001",
      "response_file": "responses/SRC-001.md",
      "response_sha256": "SHA-256 of this response",
      "scores": {
        "conclusion": 0,
        "source_fidelity": 0,
        "attribution": 0,
        "minhag_and_scope": 0,
        "uncertainty": 0,
        "usefulness": 0
      },
      "critical_failure": false,
      "rationale": "Replace example scores with evidence-backed judgments."
    }
  ]
}
```

The zeros above are illustrative schema values, not results. Score a real run:

```sh
python3 benchmarks/score.py benchmarks/runs/RUN/judgments.json \
  --output benchmarks/runs/RUN/report.json
```

Report assessed cases and total suite size, case-level failures, source-access
failures, abstentions, rubric totals, and unassessed cases. Do not call an
unassessed case a pass. Report baseline and skill results together before
claiming improvement. The separately recorded baseline and skill runs are
compared in [RESULTS.md](RESULTS.md).

## What a stronger study needs

The [proposed comparison with practicing rabbonim](RABBI-COMPARISON.md) defines a
possible human study. It has not been conducted.

Recruit independent qualified reviewers; agree how to represent legitimate
differences; reserve unseen cases; cover additional areas of halakhah; use fresh
sessions and repeated runs; randomize review order; report disagreements and
adjudications. Disclose failures and exact model/tool versions. Do not compare
AI performance with “rabbis” without defining and actually evaluating that group
on an appropriate, consented task.

The source fetcher's unit tests and CI checks assess the software infrastructure.
They never enter the halakhic score denominator.
