# Phase 0 Consolidation Review

Date: 2026-10-22

Status: Draft for Human Research Director review; documentation and research design only.

Subsequent authorization: after this consolidation was prepared, the Human Research Director explicitly requested committing and pushing the five new drafts, then stopping. That authorization covers repository publication of these drafts only; it does not accept the ADRs, authorize experiments or implementation, or include the pre-existing untracked whitepaper and proposal. Statements below about the initial no-publication boundary describe the drafting scope before this subsequent instruction.

## Findings and inspection scope

All requested materials were found at the supplied paths: whitepaper, decision proposal, earlier review, RQ-001, combined ADR draft, Concept 001, roadmap, README, CONTRIBUTING and SECURITY. No requested material is missing. The original two-ADR separation is recoverable without deleting history. The proposal and RQ draft already agree on Researcher-owned final revision and a separate Oracle; the whitepaper's shorter P1 path needs a proposed clarification, not a silent edit.

At this iteration's start, Git showed untracked `docs/architecture/` and `docs/proposals/`, with no tracked modifications. Existing documents remain unchanged. The prior turn's commit/push authorization does not apply to this iteration: the latest instruction authorizes five local drafts and explicitly excludes publication. Linked whitepaper/proposal files are available locally; their presence in a future published tree must be checked separately.

Public-source inspection was limited to official Python documentation and pinned CPython documentation/license files for the examples. No legacy repository or employer-specific source was accessed, and no private report was used as evidence. The whitepaper's broader literature bibliography was not newly validated. The new findings are document analysis, not runtime, model-performance or security-test results.

## Consistency matrix

| Topic | Whitepaper | Decision proposal | Consolidation treatment |
|---|---|---|---|
| Human-directed evidence | §§0, 4–5, 9–10 | §§0, 2 Q3, 3.3 | Preserve human scope/resource/exception/publication authority and independent frozen Oracle; aligns with Concept 001 and README |
| Execution versus semantics | §§4–5; ADR-002 in §13 | Q3 | ADR-002 owns deterministic control; models provide semantic outputs, never authorization |
| Adaptive scope | §§1, 6.2, 7 | Q1 explicitly distinguishes platform and study | Pre-execution frozen selection is RQ-001-only; future adaptive work remains possible under separate protocols |
| Final revision | §6.2 omits return to Researcher | Q2 specifies one bounded revision | ADR-002 and examples specify Researcher finalization; proposed whitepaper correction below |
| Reviewer versus Oracle | §§5.3, 9.4 | Q2/Q3 | Findings are candidates; Oracle grades the final artifact. Fresh context does not imply independent errors |
| Contracts and identity | §§4.4, 6, 8 use roles/sessions plus ambiguous run/trial IDs | Q4 proposes five contracts and attempt lineage | Task, Session, Handoff, Artifact, Verdict plus distinct trial/execution/attempt; proposed run_id mapping remains reviewable |
| Unknown limits | §§8.2, 10; enforcement remains proposed | Q3 distinguishes reservation, observation and unknowns | Unsupported or unknown essential capability blocks dispatch under a claimed guarantee; no model promises substituted |
| ADR split | §13: 001 repository, 002 control | §3.1 requests split | Two new proposed drafts; old combined draft preserved and reference repair listed |
| Paper examples | §§9.1, 11 | Q5 and §4 | Two original licensed-document examples; no Python execution, model trial or benchmark result |
| Extensibility | §§4.4, 7.3 | Q1/Q4 defer generic machinery | Record future simplification hypothesis; no new RQ-001 treatment or speculative framework |
| Provenance | §§0, 10 include independence | Q5 and §3.2 | Current instruction is stricter: no inspection/inference/reference of employer-specific work; new examples depend only on permitted public documentation |
| Schedule/status | §§11–12 propose 12 weeks | §4 timeboxes and separate gates | Maintain concept/early research status; roadmap stages remain candidates, not committed deliveries |

CONTRIBUTING's evidence/assumption distinction and SECURITY's documentation-only posture remain accurate. A draft decision, completed paper example, or hash check does not demonstrate an operational system.

## ADR history and proposed corrections — approval requested, not applied

The requested filenames below take precedence over the proposal's suggested filenames. New drafts remain proposed; there is no accepted ADR yet.

| Existing reference | Proposed correction after human approval |
|---|---|
| `docs/decisions/ADR-001_Independent_Orchestrator_Draft.md` title and combined scope | Add a dated history note linking both new drafts and stating its historical combined-draft status. Preserve its original contents; mark supersession only if/when decisions are accepted |
| `Research_Team_Architecture_Review_v0.1.md` integration table and recommendation | Add a dated consolidation addendum linking split ADRs, while retaining the earlier observation that numbering conflicted |
| `Research_Question_001_Draft.md` final References paragraph | Link ADR-001 for provenance and ADR-002 for authority; retain the prior combined draft as history if useful |
| Whitepaper §13 | Link ADR-001 Repository Independence and Provenance Boundary and ADR-002 Independent Deterministic Orchestrator; retain ADR-003/004 as deferred proposals |
| Proposal §3.1 candidate paths | Add links to the actual requested filenames; do not erase its earlier recommendations |
| Whitepaper §6.2 and §§5.2/8.1 | Clarify Researcher return/final revision and reconcile required uncertainties output; approve actual serialized artifact format before implementation |
| Whitepaper §§6.1/8.2 | Resolve run/trial/attempt identity and distinguish paused human hold, terminal execution and Oracle verdict using the new conceptual definitions |

These are specific requested future edits, not permission to alter existing files now. No README, roadmap, contribution or security-policy rewrite is necessary for the five drafts. Any publication review of existing background sections should be separately scoped; it must not introduce private-system detail or claim those assertions were verified.

## Requirements, constraints, hypotheses and observations

| Category | Statements |
|---|---|
| Current binding task constraints | Documentation only; five requested drafts; public reusable non-BSP/SoC/AOSP sources; strict independence/confidentiality; no experiments, paid API use, implementation, commit, push or publication |
| Direction to express in proposed ADRs | Deterministic execution authority, semantic agents, human approvals, explicit contracts, separate Oracle and honest unknowns; direction authorization does not accept the ADRs |
| RQ-001 experimental constraints | Frozen pre-task policy, fixed model configuration, bounded Researcher revision, equal task-level ceilings, no runtime adaptation or answer-key leakage; not permanent architecture restrictions |
| Unapproved operational choices | Exact retry/failure semantics, serialized artifacts, run_id alias, policy features, provider, numeric caps and thresholds, corpus packaging and trial counts |
| Untested hypotheses | Selective review improves trade-offs; independent review improves final quality; handoffs reduce loss; control is economical and enforceable through a selected interface; future role consolidation reduces burden |
| Observed in this iteration | Required files exist; ADR naming conflict exists; pinned public document bytes, relevant passages and permission statements were inspected and hashed |

## Methodology and provenance concerns

The [paper examples](../research/Task_Oracle_Examples_v0.1.md) supply visible tasks, exact source scopes/digests, source permissions, output fields, hidden keys, critical-error rules and proposed rubrics. They are development material from two documents within one project, not independent corroboration or a representative dataset. Do not make the simple/multi-source distinction a post-hoc proxy for known error rates. New held-out tasks must be separated by source/topic family before tuning the policy.

The Oracle is independent of agent self-assessment, but its author has seen the tasks and keys. Human verification is still pending. Blinded grading, documented ambiguity handling and versioned keys reduce bias without eliminating it. Same-model Reviewer errors may correlate; P0/P1 differ in instructions and context as well as agent count. No pure agent-count causal effect follows from this design.

The example file contains answers by request. Section headings are not access control: future agents must receive extracted bundles only, with no access to this file, repository Oracle text, search index or prior design conversation. No such bundles or isolation were created. The example tasks are unsuitable as untouched holdout after exposure.

The [Python license declaration](https://docs.python.org/3.14/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python) and pinned license texts support a reusable source choice with notice obligations. The example manifest documents exact files and fragment digests. No corpus is vendored; future extraction/distribution must retain required notices and agreement and record transformations. Unknown permission, unavailable pinned bytes or mismatched digests blocks use; do not substitute unverified material. This does not license the research repository or approve model transmission/publication.

Task-level rubric pass rules are now concrete proposals; RQ-level quality floor, allowed degradation and efficiency thresholds remain unset. Two tasks cannot validate adaptive benefit. Retain all scheduled and attempted outcomes, failures and unknown usage; grading and setup time are separate from operational human effort. A missing provider capability cannot be treated as an enforced budget, isolation or cancellation guarantee.

## Remaining decisions and readiness

| Open decision | Needed before |
|---|---|
| Accept or revise split ADRs and authorize the listed history/link annotations | Changing existing documents or calling either ADR accepted |
| Verify source-to-key reasoning and choose final logical/serialized output fields | Freezing the two example contracts |
| Approve malformed-review termination, retry policy, human-hold/resume and identity mapping | Any execution specification |
| Complete corpus notices, extraction manifests and Oracle isolation plan | Transmitting any example to a future agent |
| Select provider/model and establish capabilities, money/token/time ceilings and unknown handling | Any paid/inference dispatch; still separately unauthorized |
| Freeze policy, holdout, repetitions/order, missingness rules and comparative thresholds | A performance pilot or adaptive-effect claim |
| Decide whether and how to publish these drafts and their linked local source documents | Git commit/push/publication; not part of this iteration |

## Schedule and next human checkpoint

A documentation-only review can fit one 4–6 hour week. Proposed timeboxes: 30–45 minutes for ADR/reference decisions; 60–90 minutes for checking both source/key/rubric pairs; 45–60 minutes for information-flow and failure-path paper walkthroughs; 30–45 minutes for resource/measurement unknowns; 30–45 minutes for recording decisions and small authorized revisions. Total 195–285 minutes (3.25–4.75 hours), leaving at least 45 minutes within a six-hour week for unexpected work. These are estimates, not recorded effort. Split across weeks if source or rubric questions remain.

Do not add model trials to that timebox. The earlier illustrative pilot of 6–10 tasks × 3 arms × 2 repetitions is 36–60 trials before retries; at ten minutes of grading each, grading alone is 6–10 hours. Reduce scope or defer P2 if the full comparison is unsustainable; label P2 untested rather than claim an adaptive result from P0/P1 alone.

Recommended checkpoint: review the two ADR drafts and both paper keys; decide whether the proposed identity/failure/output conventions are acceptable; approve or defer the precise history/link corrections; record remaining budget/provider/policy decisions as unresolved. Then authorize only the next bounded documentation step if needed. No implementation or experiment gate is satisfied merely by completing these five drafts. Stop here for Human Research Director review.

## Deliverables

- [ADR-001 — Repository Independence and Provenance Boundary](../decisions/ADR-001_Repository_Independence_Draft.md)
- [ADR-002 — Independent Deterministic Orchestrator](../decisions/ADR-002_Independent_Orchestrator_Draft.md)
- [Task/Oracle Examples v0.1](../research/Task_Oracle_Examples_v0.1.md)
- [Future Research Questions v0.1](../research/Future_Research_Questions_v0.1.md)
- This consolidation review.
