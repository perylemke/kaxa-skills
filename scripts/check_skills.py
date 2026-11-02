#!/usr/bin/env python3
"""Validate kaxa-skills layout and SKILL.md files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

EXPECTED: list[tuple[str, str]] = [
    ("kaxa-list-providers", "list_providers"),
    ("kaxa-create-sandbox", "create_sandbox"),
    ("kaxa-sync-repository", "sync_repository"),
    ("kaxa-exec", "exec"),
    ("kaxa-list-sandboxes", "list_sandboxes"),
    ("kaxa-inspect", "inspect"),
    ("kaxa-restart", "restart"),
    ("kaxa-upgrade", "upgrade"),
    ("kaxa-destroy", "destroy"),
    ("kaxa-create-snapshot", "create_snapshot"),
    ("kaxa-list-snapshots", "list_snapshots"),
    ("kaxa-restore-snapshot", "restore_snapshot"),
    ("kaxa-delete-snapshot", "delete_snapshot"),
    ("kaxa-publish-api", "publish_api"),
    ("kaxa-set-url-auth", "set_url_auth"),
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## When to use",
    "## Call",
    "## Result",
    "## Mistakes",
]

DESTRUCTIVE = {"kaxa-destroy", "kaxa-restore-snapshot", "kaxa-delete-snapshot"}

WORKSPACE_REFS = {
    "kaxa-create-sandbox",
    "kaxa-sync-repository",
    "kaxa-exec",
    "kaxa-publish-api",
}

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NAME_LINE = re.compile(r"^name:\s*(.+)\s*$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    block = m.group(1)
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip()
    return out


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)


def main() -> int:
    errors = 0

    for dirname, tool in EXPECTED:
        skill_dir = SKILLS / dirname
        skill_md = skill_dir / "SKILL.md"
        if not skill_dir.is_dir():
            fail(f"missing directory {skill_dir.relative_to(ROOT)}")
            errors += 1
            continue
        if not skill_md.is_file():
            fail(f"missing {skill_md.relative_to(ROOT)}")
            errors += 1
            continue

        text = skill_md.read_text(encoding="utf-8")
        lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
        if lines >= 500:
            fail(f"{skill_md.relative_to(ROOT)} has {lines} lines (max 499)")
            errors += 1

        meta = parse_frontmatter(text)
        name = meta.get("name", "")
        if name != dirname:
            fail(f"{skill_md.relative_to(ROOT)}: name {name!r} != directory {dirname!r}")
            errors += 1

        desc = meta.get("description", "")
        if not desc:
            fail(f"{skill_md.relative_to(ROOT)}: empty description")
            errors += 1
        elif tool not in desc:
            fail(f"{skill_md.relative_to(ROOT)}: description must mention tool {tool!r}")
            errors += 1
        if re.search(r"\b(I can|You can)\b", desc, re.I):
            fail(f"{skill_md.relative_to(ROOT)}: description must not use first/second person")
            errors += 1

        for section in REQUIRED_SECTIONS:
            if section not in text:
                fail(f"{skill_md.relative_to(ROOT)}: missing section {section}")
                errors += 1

        if dirname in DESTRUCTIVE and "## Ask first" not in text:
            fail(f"{skill_md.relative_to(ROOT)}: missing ## Ask first")
            errors += 1

        if dirname in WORKSPACE_REFS and "workspaces.md" not in text:
            fail(f"{skill_md.relative_to(ROOT)}: must reference workspaces.md")
            errors += 1

    ws = SKILLS / "kaxa-exec" / "workspaces.md"
    if not ws.is_file():
        fail(f"missing {ws.relative_to(ROOT)}")
        errors += 1

    extra = sorted(
        p.name
        for p in SKILLS.iterdir()
        if p.is_dir() and p.name not in {d for d, _ in EXPECTED}
    )
    if extra:
        fail(f"unexpected skill directories: {', '.join(extra)}")
        errors += 1

    if errors:
        print(f"{errors} check(s) failed", file=sys.stderr)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
