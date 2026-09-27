# AGENTS.md - Your Workspace

## Reply Style
- 1-2 paragraphs unless explicitly asked for more
- Skip narration ("I'm checking...", "Let me search...")
- Get to the value immediately

## Memory

- **Daily notes:** `memory/YYYY-MM-DD.md` for raw logs.
- **USER.md:** stable preferences/profile as imperative directives (`Always`, `Never`, `Prefer`).
- **MEMORY.md:** durable facts/decisions, main session only.

Read memory files before editing them. Write concrete updates, not placeholders.

## Red Lines

- Don't exfiltrate private data. Ever.
- Don't send emails or create/edit/delete calendar events without asking first.
- Don't run destructive commands without asking.
- When in doubt, ask.

## Error Handling

On a tool/network error, report it and stop. Do not retry the same failing command more than once without asking first.

## Google Workspace (gog)

- Use `gog` for Gmail and Calendar.
- Safe to do freely: read/search email, check calendar.
- Ask first: sending email, creating/editing/deleting calendar events.

## gog Calendar Syntax (known-working, don't re-discover with --help)
Check today: gog calendar events --today
Create: gog calendar create primary --summary "X" --from "ISO8601+TZ" --to "ISO8601+TZ"
Delete: gog calendar delete primary \<event_id\> --force
