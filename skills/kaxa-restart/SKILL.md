---
name: kaxa-restart
description: Calls the kaxa MCP tool restart to reboot a sandbox from disk. Use when processes need a clean boot, not when deleting the sandbox or restoring a snapshot.
---

# restart

## Overview

Reboots the sandbox; running processes stop.

## When to use

- Recover from a bad process state without destroying data.

Not `destroy`. Not `restore_snapshot`. E2B also auto-pauses after ~1 hour idle; next `exec` resumes without restart.

## Call

`list_providers`: need `restart` capability (E2B, Docker, Daytona; not Modal, Sprites, or Blaxel—check live response).

Required `name`. Optional `provider`.

## Result

`id`, `provider`, `status`.

## Mistakes

- Restart when the user asked to delete (`destroy`).
- Calling on providers where `restart` is false (error names providers that support it).
- Expecting restart to pull latest local Git changes from the host.
