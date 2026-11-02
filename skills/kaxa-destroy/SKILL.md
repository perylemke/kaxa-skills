---
name: kaxa-destroy
description: Calls the kaxa MCP tool destroy to permanently delete a sandbox. Use only when the user asks to remove a sandbox and accepts data loss.
---

# destroy

## Overview

Permanently deletes a sandbox and its data. No undo.

## Ask first

Call only when the user explicitly asks to destroy/delete the sandbox.

## When to use

- User-requested cleanup after work.
- Tear down billable sandboxes.

Not for pause (E2B idle pause). Not for snapshot delete (`delete_snapshot`).

## Call

Required `name`. Optional `provider`.

Provider must be available.

## Result

`id`, `provider`, `status`.

On Modal, Docker, and Daytona, snapshots outlive the sandbox. On Sprites, checkpoints are destroyed with the sprite.

## Mistakes

- Destroying without user confirmation.
- Expecting destroy to remove snapshots on Modal/Docker/Daytona.
- Destroying to "refresh" code—use new `create_sandbox` with `sync` instead.
