---
name: ss14-upstream-maintenance
description: Upstream/fork maintenance guidance for {FORK_NAME}. Use when touching non-{FORK_DIR} files, reviewing upstream diffs, preserving path similarity, porting fork code, marking {EDIT_MARKER}-Edit blocks, or deciding whether an engine/content change is allowed.
---

# SS14 Upstream Maintenance

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

This skill protects {FORK_NAME} from painful upstream merges.

## Workflow

1. Open `references/engine-boundaries.md`.
2. Open `references/fork-only-content.md`.
3. Open `references/edit-strategy.md`.
4. Open `references/edit-types.md` and `references/path-similarity.md` for ports.

## Rules

- Never edit `RobustToolbox`.
- Prefer `{FORK_DIR}` fork-owned files.
- Mark every non-`{FORK_DIR}` change with narrow `{EDIT_MARKER}-Edit` blocks.
- Keep upstream diffs small and intentional.
- Preserve upstream path similarity for ports so future merges and blame remain readable.
- Do not use conflict-avoidance hacks to hide meaningful upstream behavior changes.

## Marker Format

Use native comments and keep the block as small as possible:

```csharp
// {EDIT_MARKER}-Start: reason
CODE
// {EDIT_MARKER}-End
```

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
