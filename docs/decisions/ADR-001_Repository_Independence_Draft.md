# ADR-001 — Repository Independence and Provenance Boundary

Date: 2026-10-22

Status: Proposed draft; not accepted. Owner: Human Research Director.

## Context and history

[Concept 001](../concepts/research-os/concept-001.md) establishes independent, human-directed, model-independent, evidence-driven research. The [whitepaper §13](../architecture/Research_Team_Architecture_v0.1.md) assigns repository independence to ADR-001 and execution control to ADR-002. The [decision proposal §3.1](../proposals/Phase_0_Architecture_Decision_Proposal_v0.1.md) recommends preserving that separation.

The earlier [combined ADR-001 draft](ADR-001_Independent_Orchestrator_Draft.md) remains unchanged as historical input. This new draft proposes the repository portion; [ADR-002](ADR-002_Independent_Orchestrator_Draft.md) proposes execution control. Neither new document silently supersedes the earlier draft or accepts a decision. The [consolidation review](../reviews/Phase_0_Consolidation_Review.md) lists reference corrections requiring approval.

## Proposed decision

Use AI-Craft-Research-OS as the independent research home. Author tasks, contracts, analysis, and any separately authorized future technical assets independently from appropriately licensed public sources or original work. No employer-specific material may be inspected, imported, reproduced, inferred, or referenced. Do not inspect or copy code, prompts, fixtures, data, or other assets from the legacy `agent-skill-automation` repository. General engineering principles suffice; historical private-system assertions are not evidence for this decision.

Every external research asset needs a provenance record identifying its author/project, public source, immutable version where available, retrieval date, exact scope and digest, reuse basis, required notices, and transformations. Record permissions for access, model transmission, and redistribution separately. Public accessibility alone is not a reuse license. Unknown ownership or permission blocks use; it is not resolved by paraphrasing an unapproved source or substituting unverified material.

Use only public, reusable, non-BSP/SoC/AOSP research inputs. Keep answer keys and grading material outside agent-visible inputs. Exclude secrets and private conversations from artifacts. Retain necessary observable evidence; do not request hidden chain-of-thought. Review source notices and data minimization before any future publication. No repository-wide license is selected by this ADR.

Human approval remains necessary for research scope, resource policies, important exceptions, and publication. Approval to read a public source or draft documents is not approval to transmit a corpus to a model provider, spend resources, run experiments, commit, or publish. Current authorization covers the five consolidation drafts only.

## Alternatives and consequences

| Option | Assessment |
|---|---|
| Independently authored research with inspectable public provenance | Proposed; preparation takes time but makes inputs and assumptions reviewable |
| Reuse legacy assets | Excluded by the current boundary; convenience does not establish provenance or authorization |
| Treat public availability as sufficient permission | Rejected; source-specific reuse obligations still apply |
| Select a project license as part of this task | Deferred to the owner; outside this documentation iteration |

This boundary supports traceability; it does not prove originality, ownership, security, or scientific validity. The [paper examples](../research/Task_Oracle_Examples_v0.1.md) demonstrate a source manifest and explicit packaging obligations, not a completed publication package.

## Acceptance and revisit

For later acceptance, the owner should confirm the two-ADR split, review the example provenance and license obligations, and authorize any historical-reference annotations. Acceptance would establish a direction only. If an intended source cannot be reliably pinned or reused, exclude it and record the blocker. Changes to this boundary require a new explicit decision with reasons; no silent expansion through a tool, agent, or dependency is permitted.
