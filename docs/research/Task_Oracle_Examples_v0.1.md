# Paper Task/Oracle Examples v0.1

Date: 2026-10-22

Status: Proposed design examples; human approval and runtime packaging pending. No task execution or model trial performed.

## Use and information boundary

These are independently authored development examples for [RQ-001](Research_Question_001_Draft.md), not held-out evaluation tasks. They use general Python documentation, not project-specific code or copied fixtures. Reading source documents and computing source hashes is provenance preparation, not executing either example. Answer keys below are proposed independently of any agent output; the human must verify and freeze them before future use.

This whole document is a human design/review artifact containing Oracle-only answers. **Never hand the whole document, this repository, or its Oracle sections to a Researcher or Reviewer.** Future packaging must extract only the explicitly agent-visible common contract, relevant source slices, and the selected task card into an isolated input bundle. Keep answer keys, grading notes, strategy-comparison thresholds and verdicts outside accessible context, paths and search indexes. No agent bundle or runtime isolation has been created here; those remain prerequisites before execution. Exposure of this document disqualifies a session from a blind evaluation on these examples.

## Public source manifest and reuse basis

Checked 2026-10-22. Python Software Foundation / CPython documentation contributors are the source project. Immutable revision: `ebf955df7a89ed0c7968f79faec1de49f61ed7cb`, resolved from release tag `v3.14.0`. Readable moving documentation pages were used for discovery only; the following pinned source bytes and line scopes define the candidate corpora.

| ID | Pinned public source | SHA-256 of full raw file |
|---|---|---|
| J | [Doc/library/json.rst](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/library/json.rst) | `8d9226d893ae02caa7c326bbe4d56283f86f1062993665f473f04fb10065c45b` |
| D | [Doc/library/stdtypes.rst](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/library/stdtypes.rst) | `98bf9fe448aed657067f78387e1248da6e503761e260ab38d737e14cccb2d1fe` |
| L1 | [Doc/license.rst](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/license.rst) | `c695d550b135e53e38807e76496d1db17d22c40e461d1f3f354c86188d3305dd` |
| L2 | [LICENSE](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/LICENSE) | `b0e25a78cffb43f4d92de8b61ccfa1f1f98ecbc22330b54b5251e7b6ba010231` |

The official [license declaration](https://docs.python.org/3.14/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python), corroborated by L1 lines 79–84, places documentation under PSF License Version 2; the separate code-example license does not replace the prose license. L2's PSF terms permit reuse subject to retaining the agreement and copyright notice; derivative redistribution also requires a change summary. This is a recorded permission basis, not an assertion that every future packaging or publication obligation is already satisfied.

No source text or code is vendored in this iteration. These tasks, scenarios and rubrics are original; factual answer keys are paraphrased with locators. Before distributing or transmitting a future extracted corpus, retain the applicable full license agreement and notices, attribute the project, and record the extraction/formatting change summary. Source selection and attribution do not grant this repository a license. If provenance, notice retention or retrieval integrity cannot be verified, block packaging rather than use a moving or unverified replacement. Public-source reuse and model transmission/publication authorization are separate gates.

Exact proposed evidence slices, all line ranges inclusive:

| Slice | Scope and purpose | SHA-256 / UTF-8 bytes |
|---|---|---|
| A-J | J lines 153–156, 194–199, 248–255; signatures, allow_nan semantics and dumps/dump relationship | `de5383ee2f6ae3257f06b8c096d073ad7121d6df744095f2e183050e629a3e30` / 999 |
| B-J | J lines 146–147, 234–236, 248–255; default ordering, sort_keys and dumps/dump relationship | `32daa36e7ba47618d2664f8e8d555c009fd684c007d145bb1e4ac6f6e571ddde` / 680 |
| B-D | D lines 4977–4978; dictionary insertion, update and reinsertion order | `6dcad3a36e5b7f8650dba06b9ab6764f82df73e153a766d5d6a7ee47de794ca6` / 153 |

Digest convention: retrieve the pinned raw UTF-8 file; split into lines; concatenate the listed ranges in listed order with LF separators and one final LF, without adding labels or blank separators. These slice hashes were computed during source inspection. Provenance metadata, notices and task text are separate components; the eventual complete bundle requires its own digest. Original line numbers remain citation locators even when slices are concatenated. L1/L2 are provenance/notice material, not extra task evidence.

## Common agent-visible contract

Use only the selected task card and its identified evidence slices. Do not execute Python, browse, install packages or infer facts from outside sources. Assess each claim as `supported`, `contradicted`, or `not_established` by this corpus, with a brief explanation and source ID/original-line locator. Distinguish documented facts from deductions about the original scenario. Do not claim empirical execution. Answer all listed claims; note uncertainty and scope limits without inventing missing evidence.

The final bundle requires a research note, claims table (claim ID, classification, explanation, evidence locator), source manifest reference, uncertainties section, and revision/disposition log. For this paper iteration these can be sections of one Markdown artifact; this proposes a logical field contract, not a silent replacement of the whitepaper's named JSON/Markdown files. Actual serialization awaits approval. If review occurs, findings separately identify claim ID, locator, severity and suggestion. The Researcher alone produces the final revision, including accept/reject/uncertain dispositions; an empty review permits a logged no-change revision. One bounded final revision, no second review loop, no human answer repair.

The policy sees only task-card features and corpus metadata before execution. Candidate feature: `requires_cross_document_reconciliation`; Example A is false and B is true by their stated objectives, not by hidden answers. A rule mapping false to P0 and true to P1 is illustrative and unapproved. All fixed arms still receive both task types in a future comparison; a task label does not itself prove review is beneficial.

## Example A — Agent-visible task card

ID/version: `TASK-PAPER-A / 0.1`. Oracle reference: `ORACLE-PAPER-A / 0.1` (key withheld). Candidate approved corpus scope: A-J only, pending human approval.

Objective: assess a short claim set about serializing non-finite floating-point values through Python 3.14.0 `json.dumps`. Assume an otherwise serializable input containing such a value and default settings except where explicitly changed. This is a document-based inquiry, not a program test.

| Required claim | Statement to assess |
|---|---|
| A1 | With default settings, dumps rejects a NaN floating-point value. |
| A2 | With allow_nan=False, serializing a non-finite float raises ValueError. |
| A3 | With allow_nan=False, the serializer replaces such a value with JSON null. |

Expected output: the common final bundle covering A1–A3. Explain the relevant option and exception without extending the result to all JSON implementations or every condition for JSON compliance. No numerical experiment budget has been approved.

## Example A — Oracle-only key and acceptance

Do not export this section to agents. Key source: [J lines 194–199](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/library/json.rst#L194-L199), with dumps linkage at lines 248–255.

| Claim | Key | Required justification |
|---|---|---|
| A1 | contradicted | Default allow_nan permits NaN encoding |
| A2 | supported | Disabling it raises ValueError for the stated values |
| A3 | contradicted | The documented result is an exception, not null substitution |

Critical errors: asserting a default rejection, denying the stated exception, or asserting null substitution in the final answer. Forbidden unsupported extensions: universal behavior across JSON encoders, or treating this one option as proof of all aspects of JSON conformance. Count such asserted extensions as critical scope errors. Explicitly stating they are not established is acceptable. Invented citations or claims of running the example are critical evidence errors.

Proposed rubric: for each of three claims, 1 classification point plus 1 evidence point for a locator that actually supports the explanation (6 points total). PASS requires 6/6, every common output field, coherent final conclusions, and zero critical errors. Missing claim or evidence fails even without a critical error. `not_established` on a required answerable claim earns no classification point. Formatting style alone is not scored. This task-level draft pass rule is not the RQ-001 comparative quality-floor threshold.

## Example B — Agent-visible task card

ID/version: `TASK-PAPER-B / 0.1`. Oracle reference: `ORACLE-PAPER-B / 0.1` (key withheld). Candidate approved corpus scope: B-J and B-D only, pending human approval. These are two documents within one source project, not independent authorities.

Objective: reconcile dictionary ordering rules with JSON output-order options. Consider an ordinary Python dictionary with string keys and integer values. Starting empty, insert `maple`, then `ash`, then `oak`. Update the value of existing `maple`. Delete `ash`, then insert `ash` again. Infer the textual key order when serialized through dumps with default settings, and separately with sort_keys=True. Values and whitespace are irrelevant to this question.

| Required claim | Statement to assess |
|---|---|
| B1 | Updating maple moves it to the end of dictionary order. |
| B2 | After the deletion and reinsertion, dictionary order is maple, oak, ash. |
| B3 | Default dumps output has textual key order maple, oak, ash. |
| B4 | With sort_keys=True, textual key order is ash, maple, oak. |
| B5 | The two documents establish that every external JSON consumer preserves this textual key order. |

Expected output: the common final bundle covering B1–B5, distinguishing container order, serialized text order and claims about external consumers. Use both source documents for the cross-document deductions. Do not run the scenario.

## Example B — Oracle-only key and acceptance

Do not export this section to agents. Ordering basis: [D lines 4977–4978](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/library/stdtypes.rst#L4977-L4978) and [J ordering note](https://github.com/python/cpython/blob/ebf955df7a89ed0c7968f79faec1de49f61ed7cb/Doc/library/json.rst#L146-L147), sort_keys at lines 234–236 and dumps linkage at 248–255.

| Claim | Key | Evidence requirement |
|---|---|---|
| B1 | contradicted | D: updating an existing key retains its position |
| B2 | supported | D plus scenario: reinsertion places ash last |
| B3 | supported | D plus J: default encoding preserves the derived container order |
| B4 | supported | J plus scenario: explicit key sorting gives the stated sequence |
| B5 | not_established | J/D describe Python behavior, not a universal consumer guarantee |

B5 is not scored as contradicted: lack of a universal guarantee in the corpus is not evidence of a counterexample. An appropriate scope explanation citing the relevant passages earns its evidence point. The apparent tension between insertion and sorted order is reconciled by the serialization option; it is not a documentation contradiction.

Critical errors: endorsing B1, giving a wrong order for B2–B4, asserting the universal guarantee in B5, fabricating evidence or execution. Forbidden unsupported claims also include equating sorted textual keys with general JSON semantic/canonicalization guarantees or independent corroboration by two organizations. Such assertions are critical scope errors; explicit limitation statements are acceptable.

Proposed rubric: 1 classification and 1 evidence point per claim (10 total); B3's evidence point requires both sources, and B2/B4 must tie the rule to the stated scenario. PASS requires 10/10, all common fields, consistent conclusions, and no critical errors. Missing evidence or claims fails. The same rubric applies regardless of strategy and evaluates the final artifact, not reviewer confidence.

## Human-only identity and handoff walkthrough specification

The following are illustrative identities, not execution records. For either task, a future trial `TR-A-P1-01` (or `TR-B-P1-01`) links a Researcher session `S-R`, drafting execution `E-D`/attempt `AT-D1`, Reviewer session `S-V`, review execution `E-V`/attempt `AT-V1`, and final revision execution `E-F`/attempt `AT-F1` in `S-R`. Artifact IDs distinguish draft, findings and final; Oracle verdict binds the final artifact digest. A retry gets a new attempt ID, not a new observation disguised as the same one.

An agent-visible review handoff may contain only: selected task/version and its visible card; approved slices and provenance/notices; draft artifact ID/digest; producing and recipient identities; permission/allocation limits; expected finding fields. Its locator allowlist is A-J for A, or B-J/B-D for B. Return only findings to Researcher for revision. **Do not include the whole file path, Oracle section, answer table, scoring annotations, verdict, or other sessions' hidden history.** Actual artifact digests are unavailable until artifacts exist and must not be invented. A digest or recipient mismatch blocks the handoff.

## Resource assumptions and measurable outcomes

Both tasks assume document-only reasoning, no executable tools and no external research network. The candidate slices contain 999 bytes for A and 833 bytes combined for B before metadata, notices and task instructions; these are measured text sizes, not token estimates. Future task-level token, money and deadline limits, stage reservations, model/provider and cancellation/usage capabilities are **unknown/unset**. No paid invocation is authorized. Proposed trial policy is zero discretionary retries; transport failures remain recorded pending an approved retry rule. P0/P1/P2 must share the approved task ceiling, and P1 review/revision costs are included.

Record final acceptance, classification/evidence subscores, required-claim coverage, critical errors, draft-to-final corrections and introduced errors, handoff validation, all-session input/output/cache usage when observable, latency and human minutes. Unknown measurements remain null with reasons. Separate setup/grading time from operational intervention. Outcomes in this document are expected keys and proposed metrics, never observed trial results.

Human rubric-check timeboxes are 15–20 minutes for A and 20–30 for B, plus 15–25 minutes to inspect the information boundary and failure cases. These are planning estimates, not measured performance. Have the human check one missing-citation case, one false assertion, a malformed review and an exhausted-budget path on paper before freezing. If the key is ambiguous, record an unresolved verdict and version a correction before experiments; do not tune the key to favor an arm.

These two small related examples cannot establish adaptive benefit, statistical noninferiority, cross-provider behavior or broad research quality. They must stay in development. A future holdout needs different source/topic families, frozen policy and scoring, plus separate execution authorization. Final bundle extraction, notices, access isolation, serialization and resource settings remain blockers to actual execution, not to reviewing these paper contracts.
