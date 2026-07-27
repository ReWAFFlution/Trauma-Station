---
name: ss14-sprite-overlays-shaders
description: Sprite, overlay, shader, RSI, and rendering resource guidance for {FORK_NAME} SS14 work. Use when adding or reviewing sprite states, overlays, shaders, icons, displacement maps, RSI metadata, visual resources, or client rendering code.
---

# SS14 Sprite Overlays Shaders

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

This is the rendering-resource companion to `ss14-graphics-generic-visualizer-appearance`.

## Workflow

1. Open `references/sprite-resource-checklist.md`.
2. Open `references/overlay-patterns.md`.
3. Open `references/shader-and-displacement-notes.md`.

## Rules

- Put {FORK_NAME} textures under `Resources/Textures/{FORK_DIR}`.
- Preserve asset attribution.
- Keep render code client-side.
- Prefer data-driven visual state over hardcoded sprite switches.
