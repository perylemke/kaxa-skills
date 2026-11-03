---
name: kaxa-set-url-auth
description: Calls the kaxa MCP tool set_url_auth to set sandbox URL access to public or provider-account-only. Use when changing URL auth after list_providers shows public_url capability, not for starting HTTP services.
---

# set_url_auth

## Overview

Sets whether the sandbox URL is public or requires a provider account (Sprites: `sprite`).

## When to use

- User wants to open or restrict URL access on supported providers.

HTTP serving is `publish_api` or create-time `api`. This tool only changes auth mode.

## Call

`list_providers`: need `public_url` capability.

Required `name`, `auth` (`public` or `sprite` only). Optional `provider`.

Invalid `auth` values error with hint to use `public` or `sprite`.

Creating with `running` (tmux) and `public` without `api` is refused at create; this tool does not add login to a raw tmux URL.

## Result

`id`, `provider`, `auth`, optional `url`.

## Mistakes

- Using on E2B, Modal, or Blaxel where public URL auth is unavailable. Blaxel `api` previews are public and this tool cannot make them private.
- Typos in `auth` (`open`, `private`).
- Expecting `set_url_auth` to publish an API process.
