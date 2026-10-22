# Future Research Questions v0.1

Date: 2026-10-22

Status: Untested research directions; no implementation requirement or experiment authorization.

## FRQ-SIMPLIFY — Architectural simplification

Hypothesis supplied by the Human Research Director:

> As model capabilities and task characteristics change, consolidating agent roles may outperform a more specialized multi-agent topology by reducing coordination and context-transfer costs.

This is a hypothesis, not a demonstrated result or a presumption that larger models make specialists unnecessary. The counter-hypothesis is that specialization and separate contexts preserve useful checking or coverage, while consolidation increases correlated omissions, distraction or context pressure. Either outcome may depend on task family and capability level.

The architecture should permit studying both scaling out and scaling down through separate role, instance, session, model, skill/tool and topology identities. A role is a responsibility; a skill is reusable instructions or knowledge; a tool is an operation. Neither a skill nor a tool implies another agent or independent review. Consolidating semantic roles never transfers approval authority or Oracle control into the semantic worker.

## Candidate future comparisons

| Dimension | Candidate comparison | Evidence needed to avoid an unsupported conclusion |
|---|---|---|
| Role consolidation | Fixed specialist workflow versus fewer agents covering the same responsibilities | Same task/output/Oracle, comparable total limits and disclosed context/instruction differences |
| Skill/tool delegation | Dedicated agent versus a role performed through a skill or bounded tool | Include tool/skill maintenance and invocation costs; do not equate instruction reuse with independent judgment |
| Coordination overhead | Message count, transferred context and revision effort across topologies | Include all sessions and failed handoffs; measure lost required evidence, not just shorter messages |
| Model capability | Repeat a fixed topology comparison at separately specified capability/model configurations | Do not attribute improvement to topology if model and workflow change together; retain capability uncertainty |
| Versioned architecture | Compare frozen baseline with a proposed simplified version | Preserve old prompts, contracts, limits, corpus and Oracle; establish new comparability conditions before runs |

Primary future question: can consolidation meet a preregistered quality floor and critical-error constraint while reducing declared resource or human-coordination costs? Candidate observations include acceptance, omission/introduced-error rates, handoff evidence loss, usage, latency, and intervention minutes. These dimensions need explicit definitions and thresholds in a separate protocol; an opaque overall score is insufficient.

## Boundaries and revisit gate

[RQ-001](Research_Question_001_Draft.md) remains the frozen pre-execution selective-review comparison. It gains no consolidation arm, model-switching treatment, learned router, skill system or runtime topology change from this document. Its single-agent arm may be conceptually relevant, but cannot answer all future simplification questions without a new design.

Revisit after a stable baseline and reliable Oracle/resource records exist, or after documented coordination burden motivates a narrower study. First select one task family and one consolidation contrast, estimate its human effort, and freeze the baseline. New model capability claims require explicit evidence; task/provider/version changes must be recorded. Report negative and inconclusive results and keep development/holdout separation. A broader factorial study is deferred because it may exceed the 4–6 hour weekly schedule.

No provider, framework, implementation date or numerical benefit is committed. Promotion of this direction to an active research question requires Human Research Director review and separate authorization.
