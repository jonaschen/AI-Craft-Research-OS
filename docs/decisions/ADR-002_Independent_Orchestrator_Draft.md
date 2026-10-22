# ADR-002 — Independent Deterministic Orchestrator

Date: 2026-10-22

Status: Proposed draft; not accepted or implemented. Owner: Human Research Director.

## Context and proposed decision

Following [whitepaper §§4–8, 13](../architecture/Research_Team_Architecture_v0.1.md) and [proposal §2](../proposals/Phase_0_Architecture_Decision_Proposal_v0.1.md), an independent deterministic Orchestrator owns execution control. Agents perform semantic work. Human approval governs scope, resource policies, publication, and important exceptions. Logical independence does not require a service, new framework, separate process, or custom runtime. Manual paper procedures can describe this boundary without claiming automated enforcement.

This restores the whitepaper's ADR-002 scope. The [earlier combined draft](ADR-001_Independent_Orchestrator_Draft.md) is preserved; repository provenance is addressed by the new [ADR-001 draft](ADR-001_Repository_Independence_Draft.md). These are proposed successors for their respective concerns, pending explicit acceptance and history annotations.

## Authority and research scope

| Responsibility | Owner and boundary |
|---|---|
| Approvals | Human approves exact contract, policy, Oracle and resource versions; important exceptions are recorded, not inferred from model text |
| Execution | Orchestrator validates permissions/capabilities, selects approved strategy, reserves resources, dispatches bounded work, records attempts, and stops |
| Semantic research | Researcher drafts and owns final revision; Reviewer supplies evidence-linked findings, not commands or verdicts |
| Evaluation | Separate frozen Oracle evaluates the final artifact; a human may apply its semantic rubric. Neither its verdict nor reviewer confidence authorizes retries |
| Evidence | Controlled records preserve identities, artifacts, usage provenance and failures; agents cannot rewrite approval, Oracle or control records |

RQ-001 freezes a pre-execution selective-review policy: P0 is one Researcher session with one bounded self-check/revision; P1 is Researcher draft → fresh Reviewer session → Researcher one bounded final revision; P2 selects P0/P1 before model execution using approved visible features. The policy cannot inspect hidden keys, observed errors, or final scores. These are experimental constraints, not permanent limits on adaptive architecture. Future topology or model decisions require a separately versioned protocol; no speculative engine is required now.

Reviewer findings identify the claim, evidence locator, issue and proposed correction. Researcher records `accept`, `reject`, or `uncertain` with a short evidence-based reason. Empty findings permit a recorded no-change final revision. Contradictory findings require explicit disposition. Proposed malformed-findings rule: preserve them, terminate the P1 attempt as invalid, and do not quietly fall back to P0. Budget exhaustion before mandatory finalization retains partial artifacts and fails task acceptance. These edge-case rules await owner review. No second review loop or hidden human repair is allowed in this proposed RQ-001 procedure.

## Minimal conceptual contracts

| Entity | Meaning and minimum binding |
|---|---|
| Task | Versioned objective, approved corpus, visible claims, output contract, Oracle reference, visible policy features, permissions, aggregate limits and approval references; no embedded answer key |
| Session | Context lifetime: session ID, agent-instance ID, role, model/provider configuration, permitted context/tools and local allocation; one session may handle multiple bounded invocations |
| Handoff | Explicit transfer: task/version, producing attempt/session, intended recipient role/session, artifact IDs/digests, corpus scope, size limit and expected outputs; no implicit full-history transfer |
| Artifact | Identified bytes: artifact ID/version/type, producing attempt/session, digest, location, provenance and visibility; final artifact differs from draft and findings |
| Verdict | Oracle ID/version, assessed final artifact/digest, claim judgments, structural checks, critical errors, acceptance and uncertainty; distinct from execution status |
| Trial | One scheduled task × strategy × repetition within an experiment; records branch/policy and all attempts, including unstarted or failed cases |
| Execution | A bounded authorized stage invocation, such as drafting, review or revision, within a trial; has its own execution ID |
| Attempt | One dispatch attempt of an execution; retry gets a new attempt ID with predecessor link, accumulated usage and reason; no hidden overwrite |

A retry is not automatically a new statistical repetition. Researcher drafting and revision can share one session while using different execution/attempt IDs. A fresh Reviewer uses a distinct session and instance, possibly the same model. Record context continuity after interruption explicitly; no assurance that a provider can resume a session is assumed. Proposed mapping of the whitepaper's ambiguous `run_id`: retire it in new contracts or define it as an explicit alias of execution ID after approval, never infer it from trial ID.

Approval binds versions. A policy or permission change requires renewed approval for affected work; it cannot retrospectively change the treatment of a completed trial. Keep final artifact identity stable for grading. Hashes identify bytes, not truth, authorship, or protection against tampering.

## Stop rules and unknowns

Before dispatch, check the approved request against permissions, capability evidence and remaining aggregate budget. Distinguish reserved, observed, estimated, reconciled, and unknown usage. Account for all sessions, revisions, retries and chargeable overhead. If an essential capability or cost/security boundary is unknown or unsupported, do not dispatch under a claimed guarantee. Return the reason to the human; any narrower research mode needs a revised approved contract. Prompt instructions alone do not enforce a limit.

| Proposed lifecycle case | Required record and consequence |
|---|---|
| Preconditions satisfied | Dispatch a new attempt within the approved execution; record resource reservation |
| Unsupported capability / unverifiable budget or permission | No dispatch; blocked reason, unknown fields and human decision needed |
| Timeout, cancellation or crash | Preserve attempt and partial output; outcome/charges may remain unknown until reconciled; no automatic replay |
| Human hold | Paused, not terminal success/failure; record remaining resources and version-bound resume approval |
| Retry | Only if a preapproved retry rule and remaining limits permit; new attempt and cumulative accounting |
| Final output ready | End execution and submit identified final artifact to the frozen Oracle; execution completion does not imply acceptance |

This is a conceptual transition outline, not a complete recoverable state machine. Process cancellation, in-flight billing, sandbox boundaries and session restoration need interface-specific evidence before implementation. Unknown security is not equivalent to safe. Tool internet, approved inference transport and third-party telemetry are distinct permissions. Future agents must not have access to Oracle keys, approval stores or arbitrary repository contents.

## Alternatives, consequences and gates

Agent-controlled authorization blurs the boundary and is rejected for this direction. A generalized platform is premature. A minimal independent control function preserves comparability, but its reliability and maintenance cost remain hypotheses. A single fixed provider can support a controlled pilot without proving portability across providers.

Keep roles, sessions, skills/tools, models and topologies distinct so future studies can scale out or consolidate roles. The [architectural simplification hypothesis](../research/Future_Research_Questions_v0.1.md) introduces no new RQ-001 arm or implementation requirement.

Before acceptance, review the authority table, identity model and failure proposals with the two [paper examples](../research/Task_Oracle_Examples_v0.1.md). Numerical budgets, provider capabilities, final policy and study thresholds remain unset. No runtime implementation, model experiment, spending, commit, push or publication is authorized by acceptance of this draft.
