---
name: ss14-porting-and-licensing
description: Porting, attribution, fork isolation, upstream merge, and license guidance for {FORK_NAME}. Use before importing code/assets from WizDen, Delta-V, Starlight, Goob Station, Trauma Station, Funky Station, Forky Station, Moff Station, Monolith,
or other SS14 forks, assets, or external repositories, and before modifying upstream files.
---

# SS14 Porting And Licensing

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Before Porting

- Identify source repository, commit, original author, and license.
- Check whether code/assets are MIT, AGPL, MPL, CC-BY-SA, CC-BY-NC-SA, or another license.
- Do not import incompatible assets or hidden-source-incompatible code.
- Preserve attribution in metadata, comments, or license files as appropriate.

## Fork Isolation

- Put new {FORK_NAME} code/assets under `{FORK_DIR}`.
- Namespace serialized types and prototype IDs with a {FORK_NAME} prefix.
- Avoid changing upstream files. If required, use tight `{EDIT_MARKER}-Edit` markers.
- Preserve path similarity under `{FORK_DIR}` so upstream equivalents are easy to compare.

## Database Porting

- Avoid modifying upstream tables.
- Prefer one-to-one fork-owned tables for {FORK_NAME}-only data.
- Namespace migrations.
- Test SQLite and Postgres paths when persistence changes.

## Bundled References

- `references/source-license-checklist.md`: source, commit, author, license, compatibility, and import decision checks.
- `references/attribution-patterns.md`: code, asset, RSI, station image, and generic attribution placement.

## Sources

See `ss14-wizden-docs` for forking tips, PRs with engine changes, generic attribution, station image specs, and PR guidelines.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
