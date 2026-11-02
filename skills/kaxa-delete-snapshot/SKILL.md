---
name: kaxa-delete-snapshot
description: Calls the kaxa MCP tool delete_snapshot to permanently remove a snapshot. Use only when the user asks to delete a snapshot id from list_snapshots.
---

# delete_snapshot

## Overview

Permanently deletes one snapshot. No undo.

## Ask first

Call only when the user explicitly asks to delete the snapshot.

## When to use

- User-requested cleanup of old checkpoints.

Requires provider with `snapshot` capability.

## Call

Required `name` (sandbox the snapshot came from) and `snapshot` (id from `list_snapshots`). Optional `provider`.

## Result

Confirmation fields from tool output; snapshot no longer appears in `list_snapshots`.

## Mistakes

- Deleting without user confirmation.
- Guessing snapshot ids instead of listing.
- Confusing with `destroy` (sandbox vs snapshot).
