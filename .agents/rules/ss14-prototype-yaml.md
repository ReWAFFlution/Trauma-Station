# SS14 Prototype YAML

Use this rule for YAML prototypes and serialized component data.

## Layout

- Prototype order: `type`, `abstract`, `parent`, `id`, `categories`, `name`, `suffix`, `description`, `components`.
- Components under `components:` are not extra-indented.
- Separate prototypes by one blank line.
- Use inline lists for categories and regular lists elsewhere.

## SS14-ART-CORE Placement

> **Config:** Actual fork directory (`FORK_DIR`) is defined in `.agents/fork-config.md`.

- New prototypes: `Resources/Prototypes/{FORK_DIR}/<Subsystem>/`.
- New locale: `Resources/Locale/en-US/{FORK_DIR}/<Subsystem>/`.
- New textures/audio: `Resources/Textures/{FORK_DIR}` and `Resources/Audio/{FORK_DIR}`.

## IDs

- Prototype IDs use PascalCase.
- FTL IDs use kebab-case.
- Fork-owned IDs should be art-core-namespaced enough to avoid collisions.
