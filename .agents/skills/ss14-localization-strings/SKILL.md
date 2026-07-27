---
name: ss14-localization-strings
description: FTL string guidance for {FORK_NAME} SS14 work. Use when adding or reviewing localization files, keys, selectors, entity arguments, prototype names/descriptions, marking names, reagent names, UI strings, and translation-ready text.
---

# SS14 Localization Strings

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

FTL is gameplay-facing API. Name it and structure it carefully.

## Workflow

1. Open `references/localization-policy.md`.
2. Open `references/ftl-naming-and-layout.md`.
3. Open `references/selectors-and-entity-args.md` for dynamic grammar.
4. Open example refs for prototypes and markings.

## Rules

- Use kebab-case, subsystem-scoped IDs.
- Put {FORK_NAME} strings under `Resources/Locale/en-US/{FORK_DIR}`.
- Use variables/selectors/functions instead of prebuilt English sentences in code.
