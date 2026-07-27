---
name: ss14-naming-conventions
description: Naming guidance for {FORK_NAME} SS14 C#, YAML, FTL, prototypes, components, systems, events, CVars, migrations, and fork-owned serialized types. Use whenever adding new names or reviewing naming consistency.
---

# SS14 Naming Conventions

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

Names are part of the API and merge strategy.

## Workflow

1. Open `references/csharp-and-ftl-naming.md`.
2. Open `references/prototype-and-resource-naming.md`.
3. Open `references/art-core-prefixes-and-namespaces.md`.

## Rules

- Namespace fork-owned serializable types, prototypes, CVars, and migrations.
- Use PascalCase prototype IDs and component names.
- Use kebab-case FTL IDs.
- Keep {FORK_NAME}-specific paths under `{FORK_DIR}`.
