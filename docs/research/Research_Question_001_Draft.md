# Research Question 001 — Adaptive Delegation

Date: 2026-10-20
Status: Draft research contract; not preregistered, approved, or executed
Research ID: RQ-001

## Question and motivation

Can adaptive agent delegation improve research-task quality and resource efficiency relative to fixed single-agent and fixed multi-agent strategies under comparable task-level resource limits?

For the first study, “adaptive” means a versioned, deterministic rule that selects whether to delegate review using only features visible before execution. It does not mean learned routing, online policy updates, progress-triggered delegation, model selection, or parallel workers. The study estimates the effect of selective review on a declared task distribution; it cannot establish that arbitrary adaptive teams are better.

This addresses Concept 001's questions about specialization, verifiable evidence, and comparable methods. A negative or inconclusive result is a valid outcome. No experiment is authorized by this draft.

## Scope and strategy contracts

Proposed domain: short evidence-checking and evidence-synthesis tasks over independently acquired, frozen public general software documentation with verified reuse permissions. No BSP, SoC, AOSP, employer, private, or legacy-repository material. No package installation or code execution in the initial task family. A model may receive only the approved corpus and task inputs; external browsing is disabled during trials.

| Arm | Procedure | Final deliverable |
|---|---|---|
| P0 — Fixed single-agent | Researcher drafts an answer, then performs one bounded self-check/revision in the same session | Final research note, claims/sources records, uncertainties |
| P1 — Fixed multi-agent | Researcher drafts; fresh Reviewer session audits the draft and approved evidence; Researcher receives findings and makes one bounded revision | Same final artifact contract, plus review findings and handoff |
| P2 — Selective delegation | Frozen pre-task rule selects exactly P0 or P1; decision and feature values recorded before model execution | Selected branch's artifacts plus policy decision |

These finalization procedures are proposals that resolve the whitepaper's unspecified review-to-final-output step. No experiment should run until the owner accepts them. P1's “independence” means separate context and responsibility, not independent model errors. The Reviewer cannot change the task, oracle, resource limits, or permissions. Findings are candidate corrections; the final answer may explicitly disagree with evidence. There is no second review loop or hidden human repair.

All arms have the same approved model/provider configuration, task inputs, Researcher instructions, final oracle, allowed tools, and aggregate resource ceiling. Role-specific instructions and context structure necessarily differ and must be frozen and disclosed. P0 can spend its available budget on its self-check; P1 must share the same ceiling across drafting, review, revision, handoff, and any charged overhead. This compares workflow packages; it does not isolate a pure “agent count” effect from context separation or review instructions.

## Hypotheses and falsification

| ID | Hypothesis | Evidence against it |
|---|---|---|
| H1 | P1 reduces consequential unsupported or incorrect claims on evidence-complex tasks relative to P0 | No improvement, correlated misses, introduced errors, or improvement accompanied by unacceptable burden |
| H2 | P2 retains acceptable quality relative to P1 while reducing resource use, and improves quality relative to P0 within an acceptable resource increase | Routing misses harmful cases, selects nearly all/none without useful differentiation, or fails either declared quality/efficiency condition |
| H3 | Explicit handoff supports auditability without excessive context loss | Unverifiable findings, missing evidence, rework, or significant handoff overhead |

H3 is descriptive in this design: there is no unstructured-handoff arm, so no causal claim that structured handoffs are superior. Security and stopping rules are eligibility constraints, not performance gains to assume.

## Task set, policy development, and holdout

Start future protocol preparation with two paper examples, not a model trial. Then consider 6–10 independently authored tasks as a feasibility pilot, with task-family diversity and a declared mix of simpler checks and multi-source synthesis. Author tasks and answer keys separately from agent-visible inputs. Record corpus origin, permission basis, version, retrieval date, hashes, transformations, and stable evidence locators. Neither answer keys nor rubric-only hints enter handoff context.

Separate development tasks used for policy design from held-out evaluation tasks before inspecting strategy outputs. Prefer splitting by source/topic family to reduce near-duplicate leakage. Lock the split, task weights, contract, prompts, oracle, policy and tie/default behavior before evaluation. The tiny resulting holdout supports case-level feasibility findings, not general population claims.

Candidate policy feature: whether the authored task requires reconciling multiple source passages rather than checking one passage. A candidate rule delegates the former to P1 and the latter to P0. This is illustrative, not frozen or known to predict benefit. Features must be available to a real task submitter without oracle access; labels derived from observed errors or hidden answer difficulty are prohibited. Record policy authoring time. Revise only on development evidence and issue a new version; do not retune on holdout outcomes.

## Oracle and acceptance contract

The owner freezes an independent answer key and rubric before held-out execution. Proposed task-specific gates are: all required artifacts parse and link; all required claims are addressed; each required claim has the correct supported verdict with a resolvable corpus locator; no critical false or unsupported claim; unresolved evidence is explicitly marked uncertain. The final protocol must list the exact required claims, acceptable answers, critical-error definitions, and treatment of extra claims. A valid locator alone does not show that evidence supports a claim.

Use deterministic checks for artifact structure and locators, then blinded human evidence assessment where semantics require judgment. The Reviewer is not the oracle. Keep grading notes with evidence references, record unblinding and grader uncertainty, and define adjudication before running. If one owner authors and grades tasks, disclose this limitation and use blinded output ordering where feasible. Oracle corrections require a new version and consistent rescoring of all affected arms; do not silently replace initial results.

Score the final deliverable after the allowed revision. Separately record draft-to-final error correction and error introduction. Reviewer detection recall is reported only where a defensible known-defect denominator exists; seeded-defect diagnostic tasks, if later added, form a separate stratum and do not replace end-to-end research quality evaluation.

## Outcomes and decision rule

Primary quality outcome: task acceptance rate under the frozen oracle. Report claim correctness/support, critical-error count, and coverage separately so a pass/fail summary does not hide failure severity.

Primary resource endpoint, proposed: total charged token usage per attempted task, retaining input/output categories and cache categories separately when available. Tokens are a provider-specific resource proxy, not universal compute or monetary cost. Also report measured/estimated money separately, wall-clock latency, and human minutes. Include all sessions, revisions, retries, failed attempts, policy/transport overhead where observable, and finalization. Report protocol development and grading effort separately from operational human intervention.

Before any trial, the owner must choose a minimum quality floor, an acceptable quality-loss tolerance versus P1, a resource-saving threshold versus P1, and an acceptable resource increase versus P0. These values are intentionally unset, not zero. P2 supports the narrow trade-off hypothesis only if it meets the quality floor, stays within the declared loss tolerance relative to P1, meets the saving threshold relative to P1, and improves quality relative to P0 within the allowed resource increase. Report every comparison even if the joint condition fails. Strict quality-and-resource dominance, if observed, is a separate stronger finding, not a prerequisite disguised as the research question.

A tiny pilot cannot establish statistical noninferiority from a small observed difference. Label threshold checks descriptive, show per-task paired differences and counts, and avoid declaring efficacy or significance. Report the quality/resource trade-off without collapsing money, time, errors, and human effort into an opaque score. If cost or usage is unavailable, narrow claims to measured endpoints; never enter unknown usage as zero or infer cash savings from subscription limits.

## Future execution and analysis controls

Proposed unit: one task × strategy × repetition trial, containing its linked sessions and attempts. Use paired tasks across arms and at least two repetitions if the approved budget permits; freeze the actual repetition count before execution. Counterbalance or randomize arm order, record the order and method, and reset contexts/workspaces across trials. Repetitions of one task are not independent task samples. Aggregate within task before summarizing across tasks using declared weights.

Run P2 prospectively using its recorded decision. Do not choose the better observed P0/P1 outcome after grading. A retrospective routing analysis may be reported separately as exploratory and cannot substitute for P2 operational evidence. Hold model snapshot/configuration constant where supported; record opaque or changing versions and unavailable stochastic controls. Exact text replay is not promised.

Retain every scheduled trial and its outcome. Timeouts, malformed outputs, budget stops, and other attempted workflow failures remain in the attempted-task acceptance denominator. Record unstarted/skipped trials separately, with counts and reasons; do not silently drop them or impute a quality score. Distinguish provider outages from workflow errors and present any exclusion sensitivity alongside the full scheduled inventory. Predeclare transport retry limits and charge all retries; no performance-driven reruns after grading. A repaired task/oracle requires versioned treatment across all arms.

If a review or revision cannot fit within the remaining budget, stop and retain the partial bundle; missing mandatory final output fails acceptance. Keep execution status separate from quality verdict. Human intervention is recorded with timing, reason, and changed inputs; any rescue answer is outside the unassisted primary comparison.

## Minimal evidence and resource contract

Each future task contract must identify the objective, corpus/input hashes, required outputs and claim IDs, oracle version, permissions and allowed inference transport, policy-visible features, model configuration, aggregate token/money/time caps, per-stage allocations, retry limit, finalization procedure, human gates, and stop behavior. Each trial record must link task, experiment, strategy, policy, attempt and session IDs; prompt/environment versions; start/end times; decisions; all artifacts/digests; usage provenance and missingness; interventions; execution status; and oracle verdict.

Reserve a bounded request allocation before each dispatch. A chosen interface must expose sufficient controls and usage for the stated cap; otherwise halt or revise the approved resource claim before execution. Remote inference and tool internet access are separate permissions. No external tracing service or public artifact upload is implicitly authorized.

## Feasibility, limitations, and readiness

At 6–10 tasks, three arms and two repetitions imply 36–60 trials before retries. Development/holdout splitting, fixture licensing, manual grading, and record reconciliation may dominate a 4–6 hour weekly schedule. First estimate two examples on paper and budget the entire workflow. If capacity is insufficient, narrow the task family or defer P2; a P0/P1-only study does not answer the full adaptive question.

Main limitations: small author-created corpus, task-selection bias, topic leakage, same-model correlated errors, imperfect blinding, role/context confounds, task-mix sensitivity, and provider drift or incomplete usage. Findings apply to this protocol and task mix, not general research productivity or provider superiority.

Readiness remains pending: owner approval of the narrow question, two permitted Task/Oracle examples, finalization contract, source manifest, policy and split, numerical thresholds, provider capabilities, total trial count, human/model budgets, and failure/analysis rules. Any subsequent implementation, experiment, spending, or publication requires its own authorization. This draft supplies no fixtures, prompts, runtime, or evaluation code.

## References and relationships

This contract is derived from [Concept 001](../concepts/research-os/concept-001.md), the [roadmap](../roadmap.md), and whitepaper §§1, 6–9, 11–12. See the [architecture review](../reviews/Research_Team_Architecture_Review_v0.1.md) for unresolved interfaces and the [ADR draft](../decisions/ADR-001_Independent_Orchestrator_Draft.md) for authority boundaries. External literature listed by the whitepaper remains a candidate bibliography; it was not independently checked for this draft and is not evidence of this project's effectiveness.
