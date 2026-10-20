# ADR-001 — Independent Orchestrator and Research Boundary

Date: 2026-10-20
Status: Proposed draft; not accepted or implemented
Decision owner: Human research director

## Numbering and scope

This is the requested ADR-001 draft. Whitepaper §13 already uses ADR-001 for repository independence and ADR-002 for deterministic orchestration. This draft combines the related boundaries for review; it neither renumbers nor supersedes those proposals. The owner must reconcile numbering and scope before accepting an authoritative ADR. No standalone tracked ADR existed at inspection.

## Context

[Concept 001](../concepts/research-os/concept-001.md) defines a human-directed, model-independent, evidence-driven research direction and does not prescribe an implementation. The [whitepaper](../architecture/Research_Team_Architecture_v0.1.md) proposes comparing single-agent, review-all, and selective-review workflows. These comparisons need stable task contracts, execution authority, resource accounting, and independent evaluation rather than agent self-certification.

The repository is currently documentation-only. No runtime, sandbox, controller, or demonstrated improvement exists. A 4–6 hour weekly schedule favors paper contracts and minimal manual procedures before reusable infrastructure. Claims about legacy audits are not evidence required for this decision, and no legacy material was accessed for this draft.

## Proposed decision

Keep this repository the independent home for research definitions and any separately approved future implementation. Independently author all new artifacts from approved public non-BSP/SoC/AOSP sources or original work. Do not import legacy code, prompts, skills, fixtures, data, histories, or runtime dependencies; do not inspect the legacy repository as a shortcut to implementation. Any future reconsideration requires a separate provenance decision and explicit authorization.

Separate deterministic execution authority from AI semantic work. The control function owns contract validation, policy decisions, dispatch authorization, limits, lifecycle transitions, evidence promotion, and stopping. Agents analyze evidence and propose results or plans; their text never constitutes permission. Human direction remains authoritative over research scope, acceptance rules, spending boundaries, and final conclusions.

“Independent Orchestrator” means logically independent of an agent's discretionary reasoning and of a provider's proprietary research state. It does not require a service, separate process, new repository, generalized framework, or custom agent runtime. Initially, approved human procedures may perform control functions; a small script can be considered only after a separate implementation decision. Deterministic control does not make model outputs deterministic.

## Authority and interface contract

| Actor/component | May do | May not do |
|---|---|---|
| Human research director | Approve exact task/policy/oracle versions, budgets, input/transmission boundaries, and final conclusions | Treat approval of a draft as experimental evidence |
| Deterministic control function | Validate approved inputs, select frozen strategy, reserve resources, authorize bounded sessions, record transitions and stop | Invent semantic truth, silently expand permissions, or retry without a declared limit |
| Researcher / Reviewer | Read approved context, produce claims, evidence links, uncertainty and review findings; request bounded actions | Rewrite task acceptance, access hidden answer keys, self-authorize delegation, raise limits, publish, or certify their own success |
| Oracle / human grader | Apply frozen checks and rubric, record evidence-backed verdicts | Trigger extra execution or retune thresholds in response to a favored strategy's result |
| Evidence store | Preserve versioned inputs, outputs, events, usage and provenance | Establish truth or authorship merely through a hash |

The smallest proposed boundary consists of: a versioned task contract; a policy decision with visible inputs, reason and budget snapshot; a session specification with role, context, permissions, model and limits; an execution result with artifacts, usage/missingness and stop reason; and a separately recorded oracle verdict. These are conceptual contracts, not committed classes, schemas, or API methods.

Keep role, agent instance, session, model, provider, and topology identities distinct. Start with P0/P1/P2 and one fixed model configuration for controlled comparisons. Preserve portable artifacts and usage provenance; add provider adapters only when a concrete second interface requires them. Unsupported capabilities must be explicit, not silently approximated.

Bind handoffs to the approved task version, originating attempt/session, intended role, input corpus, artifact digests and expected outputs. Finalization and bounded revision must be specified before comparing quality. Preserve attempt lineage and failures; separate execution completion from research acceptance. A fresh Reviewer context does not establish independent errors.

## Security, resources, and provenance

Default future tools to read-only approved inputs, bounded output locations, and no research-network access. Permit remote inference only through separately approved transport and data boundaries; telemetry and tool browsing are distinct permissions. Approval records, oracle keys, and controller evidence must not be agent-writable. Treat documents and model/tool outputs as untrusted data and validate requests and paths independently of their instructions.

Before each request, require an enforceable allocation within the aggregate task budget, including all sessions, revisions, retries, and charged overhead. Stop when permissions, remaining budget, or interface capabilities cannot be established. Record raw provider usage and estimates separately; unknown usage remains unknown. If an interface cannot bound spend, do not claim a hard monetary guarantee. Cancellation, in-flight accounting, crash recovery and retry semantics remain contract work before implementation.

Source records must establish origin, version, permissions, allowed transformations and redistribution. Public visibility alone is insufficient. Exclude unclear ownership, employer materials, and BSP/SoC/AOSP domains. Do not record secrets or private conversations; retain only necessary observable execution evidence, not hidden chain-of-thought. Public traces require data minimization and human review. The repository's lack of a selected license remains unchanged.

## Alternatives considered

| Alternative | Assessment |
|---|---|
| LLM supervisor owns control and authorization | Blurs policy enforcement with semantic judgment and changes the experimental treatment; not proposed for the first study |
| Reuse a legacy automation system | Violates the current independence boundary and introduces unreviewed provenance and behavioral confounds; excluded |
| Build a provider-neutral orchestration platform now | Adds adapters, lifecycle machinery and maintenance before the research requires them; defer |
| Use a vendor SDK as the source of truth | May simplify later execution, but SDK traces and handoffs do not define this project's acceptance or permission policy; evaluate only after contracts are fixed |
| Human-managed contracts and sessions | Preferred initial control procedure for paper walkthroughs and a separately authorized feasibility step; record interventions and avoid claiming automated enforcement |

## Consequences and trade-offs

Benefits sought: inspectable authority, stable comparison boundaries, explicit failure accounting, and evidence that can outlive one framework or provider. These are design goals, not demonstrated gains. Costs include manual contract preparation, oracle maintenance, reconciliation, and potentially duplicated session overhead. Control-layer defects, delayed billing, correlated model mistakes, and compromised tools remain risks. A deterministic controller is neither a correctness oracle nor a security proof.

The design deliberately postpones runtime routing, learned policies, concurrent workers, peer messaging, schedulers, general adapter systems, and UI. It permits negative results and a manual research workflow. Future complexity needs a demonstrated task-level need and separate approval.

## Acceptance and revisit conditions

Accept this ADR only after the owner resolves numbering, confirms independent provenance boundaries, accepts the authority table, and reviews the linked [RQ001 draft](../research/Research_Question_001_Draft.md). Acceptance records a design direction, not permission to build or run it.

Before any implementation authorization, require two paper Task/Oracle examples, finalization and handoff semantics, supported model-interface capabilities, aggregate budgets and usage assumptions, state/attempt/stop rules, and a feasible weekly work estimate. Before claiming enforcement later, verify rejection of unauthorized actions, contract changes, invalid artifacts and exhausted budgets, plus timeout/cancellation and retained failure records. No such verification has occurred in Phase 0.

Revisit this decision if manual control materially prevents a credible comparison, a second provider exposes a real portability gap, budget enforcement cannot meet the declared guarantee, or evidence shows a different topology is necessary. Version any revision and state which earlier results remain comparable. Do not reopen legacy reuse or increase autonomy by implication.

## Phase 0 outcome

Decision remains proposed. Only the review, RQ001, and this ADR draft are delivered. No orchestrator, runtime, router, evaluation framework, experiments, additional model calls, or legacy imports are included. The owner separately authorized committing and pushing these three drafts; that repository action does not constitute design acceptance or permission for the next research phase.
