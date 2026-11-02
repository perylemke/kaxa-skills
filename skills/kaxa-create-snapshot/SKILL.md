---
name: kaxa-create-snapshot
description: Calls the kaxa MCP tool create_snapshot to save sandbox filesystem state. Use when the user wants a restore point before risky changes, after list_providers shows snapshot capability.
---

# create_snapshot

## Overview

Saves the sandbox filesystem for later restore on providers with snapshot support.

## When to use

- User-requested checkpoint before experiments.

Requires `snapshot` in `list_providers`. Not on E2B or Blaxel in kaxa.

## Call

Required `name`. Optional `provider`, `comment` (max 256 bytes, no control characters, no secrets).

Snapshot includes everything on disk, including secrets written in the sandbox. Sprites checkpoints exclude `/tmp` (memory).

## Result

Snapshot `id`, `sandbox`, `provider`, optional `comment`, `created_at`. Use `id` with `list_snapshots`, `restore_snapshot`, and `delete_snapshot`.

## Mistakes

- Putting secrets in `comment`.
- Assuming `/tmp` on Sprites is snapshotted.
- Snapshots on providers without `snapshot: true`.
