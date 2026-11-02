---
name: kaxa-list-snapshots
description: Calls the kaxa MCP tool list_snapshots. Use when finding snapshot ids for restore_snapshot or delete_snapshot, or auditing saved sandbox states after list_providers shows snapshot capability.
---

# list_snapshots

## Overview

Lists snapshots with provider and source sandbox for each entry.

## When to use

- Before `restore_snapshot` or `delete_snapshot` to obtain snapshot `id`.
- Audit saved states.

Requires `snapshot` capability on the provider (`list_providers` first). E2B and Blaxel have no snapshots in kaxa.

## Call

Optional `name` (sandbox) and optional `provider`. Omit both to search every configured provider.

## Result

`snapshots[]` with `id`, `sandbox`, `provider`, optional `comment`, `created_at`.

Partial provider failures go to `warnings`. Use returned `id` values in restore/delete, not guessed names.

Modal snapshots expire after 30 days and list only on the machine that created them. Docker and Daytona snapshots persist until deleted and list from any machine.

## Mistakes

- Restoring without listing ids on Modal from another host.
- Expecting snapshots on providers without `snapshot: true`.
- Confusing snapshot `id` with sandbox `name`.
