---
name: kaxa-upgrade
description: Calls the kaxa MCP tool upgrade to move a sandbox to the latest provider platform version. Use when the user requests a platform upgrade, not for code deploys or snapshot restore.
---

# upgrade

## Overview

Upgrades the sandbox to the provider's latest platform version where supported.

## When to use

- Explicit user request to upgrade platform/runtime.

Not for application updates (use `exec`). Not available on all providers.

## Call

`list_providers`: need `upgrade` capability.

Required `name`. Optional `provider`.

If unsupported, the error lists providers that offer upgrade.

## Result

`id`, `provider`, `status`.

## Mistakes

- Calling upgrade on Daytona/E2B/Modal when capability is false.
- Confusing with `restart` or `restore_snapshot`.
