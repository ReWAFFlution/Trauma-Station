---
name: ss14-databases-migrations
description: Database and EF Core migration guidance for {FORK_NAME} SS14 work, including fork-owned tables, SQLite/Postgres compatibility, namespaced migrations, server database projects, and avoiding upstream table churn.
---

# SS14 Databases Migrations

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Rules

- Avoid modifying upstream tables.
- Prefer {FORK_NAME}-owned tables with one-to-one relations for fork-only data.
- Namespace migrations and model types clearly.
- Test SQLite and Postgres when schema or query behavior changes.
- Keep persistence out of predicted simulation logic.
- Do not store player-facing text or prototype IDs in ways that block localization or future prototype changes.

## .NET 10

The repo uses EF Core 10 packages. Check `Directory.Packages.props` and existing migration patterns before adding code.

## Bundled References

- `references/efcore-fork-rules.md`: fork-owned tables, namespaced models/migrations, and upstream table boundaries.
- `references/migration-validation.md`: SQLite/Postgres validation and review checklist.

## Placement

- Shared database models: database-specific shared project if existing pattern requires it.
- Server persistence: `Content.Server.Database` or `Content.Server/{FORK_DIR}` according to local pattern.
- Do not touch RobustToolbox persistence.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
