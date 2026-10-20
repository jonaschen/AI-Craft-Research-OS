# Research Team Architecture Review v0.1

Date: 2026-10-20
Status: Draft for owner review; no implementation authorization
Scope: Phase 0 — Architecture Review and Research Contract Preparation

## Executive assessment

The architecture is consistent with the human-directed, model-independent, evidence-driven principles in Concept 001. Its strongest choices are separating semantic work from execution authority, retaining failures and unknown usage, and making the team an experimental subject rather than assuming that more agents help. It is suitable as a research direction, but is not yet an implementable or approved contract.

The main blockers are an undefined final-output procedure after review, incomplete authority and lifecycle interfaces, unenforceable budget assumptions, and an unspecified evaluation decision rule. Resolve these on paper before building a controller. A frozen-document evidence-checking pilot is a more manageable first scope than combining document research, Python execution, routing, and platform development.

No benefits, security guarantees, or reproducibility guarantees have been demonstrated by this review.

## Inspection and evidence boundaries

Inspected README, CONTRIBUTING, SECURITY, roadmap, Concept 001, publication record, research-question issue template, bootstrap handoff, Git inventory/status/history, and the complete [architecture whitepaper](../architecture/Research_Team_Architecture_v0.1.md). No AGENTS.md was found in the inspected repository or ancestor locations. The bootstrap handoff supplies historical context, not current publication authorization.

At inspection, HEAD was `cf2af95`; tracked content was documentation and repository metadata. Git status showed only `?? docs/architecture/`; the architecture was present locally but untracked. There was no tracked implementation or standalone ADR. No legacy repository, private audit report, external reference page, model API, or experimental system was accessed. The whitepaper's references and prior-audit assertions were read as attributed statements, not independently verified findings. This is a review of supplied repository documents, not a literature validation exercise.

The current assignment limits document creation to the three requested drafts. The whitepaper §15's proposed additional files and the broader Phase 0 deliverables in §11 remain future work. Existing documents are unchanged. The owner's subsequent instruction authorizes committing and pushing these three drafts only; it does not authorize implementation or adding the untracked whitepaper. Architecture links resolve locally but will not resolve in the published Git tree until the owner separately includes that source document; the drafts must be read with this availability limitation.

## Consistency and integration

| Existing source | Assessment | Proposed treatment |
|---|---|---|
| README and Concept 001 | Strong alignment on human authority, evidence, and no demonstrated improvement | Preserve exploratory status; architecture prose describing capabilities remains proposed |
| Roadmap | Research definition precedes reproducible experiments; stages are candidates | Treat whitepaper W01–W12 as planning hypotheses, not delivery commitments |
| CONTRIBUTING and SECURITY | Documentation-only posture and public provenance constraints | Do not imply a sandbox, agent runtime, or permission system already exists |
| Publication record | Distinguishes declaration, verification, and publication | A draft or Git push is not architecture approval or evidence of technical capability |
| Whitepaper §13 | ADR-001 means repository independence; ADR-002 means deterministic orchestration | Requested ADR-001 draft combines these concerns provisionally and explicitly records the numbering conflict |
| Whitepaper §§3, 17 | Describes unavailable private audit reports and legacy observations | Do not use these as acceptance evidence or import them into research artifacts; review public suitability separately before publishing the whitepaper |

## Requirements versus hypotheses

Here, “requirement” means a constraint to preserve in a proposed contract, not an approved implementation commitment.

| Classification | Items | Evidence needed |
|---|---|---|
| Research and provenance requirements | Human owns boundaries and conclusions; independent authorship; public permitted non-BSP/SoC/AOSP inputs; no legacy imports; publication approval | Inspectable source records and owner review |
| Proposed control requirements | Agents cannot grant permissions, change acceptance rules, authorize retries, or expand budgets; all attempts and interventions retained | Later enforcement checks covering denial, cancellation, and failure paths |
| Proposed evidence requirements | Versioned contracts, inputs, prompts, policies, output identity, oracle, all-session resource accounting; unknown is not zero | Manual contract walkthrough first; later trace validation |
| Empirical hypotheses | Reviewer improves quality; selective review improves trade-offs; handoffs reduce loss; a thin controller is sufficient and economical | Held-out comparisons and failure analysis; no assumption of positive results |
| Engineering hypotheses | Hard limits can be enforced through a chosen CLI/API; provider usage is sufficiently observable; clean session separation is available | Provider-specific capability evidence before selecting the interface |
| Deferred choices | Learned routing, multiple providers, worker pools, peer messaging, parallel execution, curator, UI | A demonstrated research need, separate protocol, and explicit authorization |

Model independence is a property of research contracts and portable evidence. One fixed provider in an initial controlled comparison is compatible with that goal; it does not demonstrate cross-provider portability. Deterministic control means reproducible decisions from declared inputs, not deterministic model answers or infallible resource enforcement.

## Findings and missing acceptance criteria

“Blocking” below means resolve before the affected experiment or implementation, not that Phase 0 document drafting must stop.

| Priority / reference | Finding | Acceptance criterion proposed for the next contract |
|---|---|---|
| Blocking — §§5–6 | P1 produces review findings, but does not say who changes the final answer. Detection is different from correction | Define a final answer artifact and bounded revision procedure; specify disagreement, no-defect, malformed-review, and budget-stop outcomes; apply the same final oracle to all strategies |
| Blocking — §§6–7 | “Adaptive” could mean static task-conditional selection or live delegation | RQ001 uses a frozen pre-execution rule only; record visible features and decision before execution; runtime adaptation requires another protocol |
| Blocking — §§8–9 | Oracle ID is not an operational oracle | Freeze answer keys, required claims, forbidden claims, citation rules, severity, passing threshold, rubric, and dispute procedure before held-out runs; prevent agents accessing keys |
| Blocking — §§4, 8 | Session specification and capability negotiation are undefined | Define contract/version reference, role, session identity, context inputs, permitted tools, model configuration, resource allocation, deadline, cancellation, output/usage/error result; unsupported capability fails closed |
| Blocking — §§7–10 | Delayed billing and in-flight requests undermine an absolute monetary cap | Distinguish reservation, observed usage, estimate, and final reconciliation; reserve worst-case permitted request cost before dispatch; stop if no defensible bound exists; label subscription usage limitations |
| Blocking — §§6, 8 | Run, trial, attempt, session, and retry identity are inconsistent; HUMAN_HOLD appears terminal and resumable | Write a transition table with actors and guards; separate execution status from oracle verdict; define pause/resume, timeout, cancellation, crash, retry lineage, and exhausted budget; never silently replay a charged request |
| High — §§5, 8 | Researcher outputs include uncertainties.md, but required_artifacts omits it | Choose one required-artifact contract; define claim/source IDs, evidence locators, schema validation, and empty/unknown handling |
| High — §§6, 8 | Handoff has an empty hash map and no contract/session/version binding | Bind task contract, producing attempt/session, recipient role/session, artifact digests and source versions; reject missing, changed, oversized, or out-of-scope inputs |
| High — §§4, 9 | “Independent Reviewer” may imply independent evidence or errors | Define a fresh context without hidden Researcher history, same approved corpus and no answer key; record shared model and correlated-error limitation; do not call it statistically independent |
| High — §§8–10 | Append-only logs, hashes, and workspace restrictions are presented without enforcement semantics | Controller owns evidence log and approval records; agents cannot rewrite them; define safe path resolution, immutable artifact promotion, crash recovery, and redaction. Hashes identify content, not truth, authorship, or tamper resistance by themselves |
| High — §§9, 11 | Many metrics, no primary comparison rule or complete workload estimate | Predeclare quality floor, efficiency endpoint, acceptable degradation, repetitions, missing-data rules, and task split; retain all failures; estimate human grading time before approving scope |
| High — §10 | “Network off” conflicts with remote model inference unless channels are distinguished | Separate approved model transport from research/tool network and telemetry; declare allowed outbound data and destinations, credential isolation, retention, and third-party tracing policy |
| Medium — §§7, 11–12 | Resource profiles and calendar deliverables imply maturity beyond current evidence | Replace profile labels with explicit limits in the future contract; use evidence gates and timeboxes, with no automatic phase advancement |

## Separation, extensibility, and security

Keep semantic planning advisory. The control boundary validates typed requests against the approved contract, records decisions, and authorizes execution. A model-proposed strategy must not bypass the frozen strategy policy. Oracle results may determine a verdict; they must not automatically grant more attempts or permissions. Human approval should bind an exact contract/policy version and scope, so a later edit invalidates stale approval.

Preserve separate role, agent-instance, session, model, and topology identifiers. A small execution record can express P0/P1/P2 without a general graph engine or provider adapter hierarchy. Add provider capability fields only when a real second interface needs them; preserve raw usage alongside normalized values and record unavailable seeds/snapshots. Reproducing a method is possible even when exact output replay is unavailable.

Treat corpus text, review output, tool results, and artifact paths as untrusted data. A workspace directory alone is not an execution sandbox; future enforcement must address path traversal, symlinks, subprocesses, credentials, network access, and process termination where applicable. For the first document-only task, disabling executable tools removes unnecessary exposure. Do not claim prompt-injection prevention based on instructions alone. Approval and oracle keys belong outside agent-writable space.

Use an independently authored source manifest: public URL or original authorship, version/retrieval date, digest, permission or license basis, allowed redistribution, and transformation history. Public accessibility does not establish reuse permission. This repository has no selected license. Exclude unclear provenance and all legacy code, prompts, skills, fixtures, traces, and data; no legacy inspection is needed. Separate access permission, model transmission permission, and publication permission. Keep sensitive raw traces out of public artifacts and preserve a documented redaction mapping where safe; do not request or publish hidden chain-of-thought.

## Feasibility and scope reduction

Twelve weeks at 4–6 hours offers a nominal 48–72 hours, before busy weeks. The whitepaper's two-week Phase 0 has only 8–12 hours for multiple contracts, fixtures, and reviews. Its full implementation-plus-pilot schedule is therefore an unvalidated capacity estimate.

Six to ten tasks × three strategies × two repetitions already means 36–60 task trials. At an illustrative ten minutes of grading per trial, grading alone takes 6–10 hours, excluding fixture creation, model wait, debugging, billing reconciliation, and reporting. More trials do not replace more independent tasks.

Prioritize two paper Task/Oracle examples, then a manual single-agent evidence record, then one explicit review handoff. Defer Python execution, routing automation, adapter frameworks, schedulers, queues, resumable workflows, generalized schemas, and dashboards. If P2 cannot be evaluated credibly within budget, report it as untested; do not substitute post-hoc selection from P0/P1 outcomes for a prospective P2 trial.

Suggested next documentation session, subject to owner authorization: 30 minutes to decide the five questions below; 60–90 minutes to author two original evidence-checking Task/Oracle examples using a permitted frozen public corpus; 60 minutes for an adversarial paper walkthrough; 30 minutes to estimate cost, grading effort, and remaining work. These are timeboxes, not promised throughput. This review does not complete the whitepaper's Phase 0 exit gate: approved examples, frozen oracle, and resource/provider decisions remain pending.

## Five architectural questions for owner review

1. Is RQ001 limited to pre-execution selective review, with a fresh review session and one bounded final revision, or is runtime delegation actually required?
2. What exact final artifact, answer key/rubric, quality floor, and degradation tolerance determine success independently of the team?
3. Which authority owns dispatch, evidence promotion, approval, cancellation, and budget reservation, and what happens when the selected interface cannot enforce a limit?
4. What is the smallest portable Task → Session → Handoff → Final Artifact contract, including identity, failure, and provenance semantics?
5. Which corpus, permissions, model interface, usage measurements, and total human/model budgets make a held-out comparison credible within 4–6 hours per week?

## Recommended disposition

Retain the architecture as a proposed direction without editing it. Review [RQ001](../research/Research_Question_001_Draft.md) and the [ADR draft](../decisions/ADR-001_Independent_Orchestrator_Draft.md), resolve the blocking paper contracts, and authorize further protocol preparation separately. Neither this review nor publication of its drafts authorizes implementation, experiments, spending, or additional agents.
