# Initial development results

**Both Posek and the no-skill baseline passed all nine selected cases. This pilot
does not demonstrate an improvement from the skill.**

Run on 2026-10-02 UTC. These are AI-reviewed development observations, not an
expert-validated halakhic accuracy rate. The answer keys were withheld from
candidate agents. Full responses, source logs, and reviewer judgments are saved.

These runs used the earlier skill wording. The current revision changes the
yeshivish register, presentation, and discovery metadata, and adds a separate
divrei Torah workflow. It has not been rerun through this psak evaluation. The
original input hashes and responses are retained. See the separate [divrei Torah
examples and review](divrei-torah/RESULTS.md) for the newer editorial forward tests.

| Condition | Assessed / suite | Passed | Rubric points | Critical failures |
| --- | ---: | ---: | ---: | ---: |
| Posek skill | 9 / 24 | 9 / 9 | 108 / 108 | 0 found |
| General assistant without Posek | 9 / 24 | 9 / 9 | 108 / 108 | 0 found |

Both conditions handled the cooked-wine blessing, the asymmetric mistaken-blessing
cases, the twelve-window claim, the two specified tefillin practices, unavailable
retrieval, urgent danger, and uncertain personal status. Both changed their answers
appropriately when the stipulated fruit category or tefillin practice changed.

The skill answer explicitly exposed the cooked/diluted translation discrepancy.
The baseline also noticed it during retrieval and used the Hebrew. Posek supplied
a verified Mishnah Berurah citation for an added tefillin timing detail; the
baseline gave the same practical timing without that additional citation. These
are qualitative observations, not evidence of superior ruling accuracy.

## Read the evidence

- [Posek responses and review](runs/pilot/REVIEW.md), [judgments](runs/pilot/judgments.json), [generated report](runs/pilot/report.json), [input hashes](runs/pilot/input-manifest.json).
- [Baseline responses and review](runs/baseline/REVIEW.md), [judgments](runs/baseline/judgments.json), [generated report](runs/baseline/report.json), [retrieval log](runs/baseline/retrieval-log.md).
- [All 24 development cases](cases.json), [source provenance](SOURCES.md), [scoring protocol](README.md).

Each review links or identifies its saved response files. Judgments contain their
SHA-256 hashes; the scorer verified those hashes while generating the reports.
The scorer aggregates explicit judgments. It does not independently determine
halakhic correctness.

## What this establishes

The initial skill can produce useful answers in these narrowly specified cases.
The bundled source helper retrieved exact live segments with edition metadata.
The scoring tool produced auditable reports from saved responses and explicit
judgments. No material error was found in the selected answers under this rubric.

The result also exposes a ceiling problem: these questions did not distinguish
the skill from the general assistant. A harder, independently curated evaluation
is needed before making performance claims.

## Limits that travel with these numbers

- Only **nine preselected cases** were run in each condition; fifteen are
  unassessed. The set is predominantly elementary Orach Chayim source reading.
- Each condition used **two multi-question sessions**, not nine independent
  sessions. Paired questions may reveal their contrast to the candidate.
- Candidate agents inherited the runtime, but the **exact model identifiers and
  generation settings were not exposed**. Equal configurations were not verified.
- Source retrieval was available for six cases. Three boundary cases prohibited
  retrieval by task instruction; this was **not a technically enforced outage**.
- The baseline used normal retrieval tools, without Posek's instructions or
  helper. The skill condition used its helper. This compares two workflows, not
  an isolated prompt change under identical retrieval implementations.
- Labels and review were **AI-generated**, with primary-source inspection.
  There was no qualified human validation; comparative grading was neither
  randomized nor blinded. Narrated source logs are not immutable tool transcripts.
- No panel of rabbis was evaluated. No general halakhic accuracy, superiority,
  robustness, unseen-case performance, or statistical significance is established.

## Software verification status

Live source retrieval and report generation were exercised. Static independent
review found and corrected packaging and account-isolation issues.

**34 offline unit tests are written but have not been run.** GitHub Actions also
checks project structure and report consistency. Under the author's CI-only
machine policy, gates were not run locally; CI is pending publication. Installation
was checked through local Codex skill discovery and Claude's resolved skill links;
an end-to-end Claude invocation was not tested. These
software checks are separate from the religious-reasoning evaluation.

The next useful study uses qualified reviewers, harder unseen cases, recorded
model settings, fresh sessions, randomized review, and controlled source access.
