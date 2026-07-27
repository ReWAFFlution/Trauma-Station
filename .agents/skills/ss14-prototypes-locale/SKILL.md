---
name: ss14-prototypes-locale
description: Prototype localization and Resources layout guidance for {FORK_NAME}. Use when adding player-visible prototypes, markings, reagents, guidebook entries, entity names/descriptions, or localized resource data.
---

# SS14 Prototypes Locale

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

Prototype data and FTL should land together.

## Workflow

1. Open `references/prototype-locale-checklist.md`.
2. Open `references/resources-map.md`.
3. Open `references/entity-marking-reagent-examples.md`.

## Rules

- New {FORK_NAME} prototypes go in `Resources/Prototypes/{FORK_DIR}`.
- New {FORK_NAME} locale goes in `Resources/Locale/en-US/{FORK_DIR}`.
- Use entity prototype localization patterns when supported.
- Keep prototype IDs and locale IDs specific enough to avoid clashes.
