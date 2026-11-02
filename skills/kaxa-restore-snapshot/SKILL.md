---
name: kaxa-restore-snapshot
description: Calls the kaxa MCP tool restore_snapshot to apply a saved snapshot. Use only when the user asks to restore, after reading snapshot_restore from list_providers and snapshot id from list_snapshots.
---

# restore_snapshot

## Overview

Restores filesystem state from a snapshot. Behavior depends on `snapshot_restore` mode.

## Ask first

Call only when the user explicitly asks to restore, especially for `in_place` (overwrites live sandbox state).

## When to use

- User-requested rollback or clone from snapshot.

Read `list_providers` → `snapshot_restore`. Read snapshot `id` from `list_snapshots`.

## Call

Required `name` (source sandbox), `snapshot` (id). Optional `provider`, `target`.

| `snapshot_restore` | `target` |
| --- | --- |
| `in_place` (Sprites) | Rejected; overwrites `name` |
| `new_sandbox` (Modal, Docker, Daytona) | Required, must differ from `name`; creates new sandbox |

## Result

`sandbox` (holds restored state), `snapshot`, `provider`, `status`. For `new_sandbox`, `sandbox` is the target name.

## Mistakes

- `in_place` restore without user confirmation.
- Omitting `target` on `new_sandbox` providers.
- Using wrong snapshot `id` from another machine (Modal listing).
