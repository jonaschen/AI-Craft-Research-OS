# Knowledge bundle v1 and release procedure

The MCP consumer in `jonaschen/ai-bsp-knowledge-skill-sets` reads compiled file bundles, never imports this repository's Python modules at runtime. `manifest.json` declares `bundle_format: bsp-knowledge`, `bundle_version: 1`, and `schema_version: 1`. Older bundles without explicit format/version must be regenerated. Existing CLI JSON remains unchanged.

Required consumer inputs: manifest, `agent/index.json`, and the human Markdown files referenced by its chunks. The complete compiler output must travel together: every file except manifest is included in manifest.outputs. SHA-256 is calculated over raw file bytes. The revision hashes inputs; bundle_sha256 hashes outputs, using sorted-key, UTF-8, indent=2 JSON plus final newline. This is drift detection, not authentication. Accept only a bundle obtained from a trusted release channel.

Chunks retain IDs, topic, version, review status, citations, original content hash and relative human paths. Consumers must not convert retrieval similarity into confidence or graph hypotheses into a confirmed diagnosis. Evaluation answers, custom data and fixtures are excluded from exports.

## Release and rollback

1. From a clean producer checkout, record `git rev-parse HEAD` as producer_commit.
2. Run the corpus tests and `python3 -m bsp_kb compile --output /absolute/new/release-directory` from experiments/bsp-kb.
3. Run `python3 -m bsp_kb check --output /absolute/new/release-directory`. Record manifest revision and bundle_sha256 alongside producer_commit in the external deployment record (not inside the bundle).
4. Configure the consumer's BSP_KB_BUNDLE to that immutable directory. Run contract and stdio tests before switching a deployed MCP process.
5. Restart with the previous directory to roll back. Do not mutate a published directory or auto-follow branch HEAD.

A deployment record must include producer_commit, consumer_commit, revision, bundle_sha256 and validation results. Packaging/transport may be chosen by deployment operators; do not include confidential materials or grant a new repository license. This integration does not require installing the separately generated skill package.
