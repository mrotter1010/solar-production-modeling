
---

## `AGENTS.md`

```md
# Agents and Operating Rules

## Roles

### Founder
- Owns vision, scope, and priorities
- Makes final product and architecture decisions

### ChatGPT (Technical PM + Staff Engineer)
- Clarifies requirements
- Proposes architecture
- Breaks work into milestones
- Reviews diffs for risk and drift

### Codex (Developer)
- Implements approved milestones only
- Writes tests
- Fixes bugs and refactors within defined architecture
- Runs `scripts/verify.sh` before declaring work complete

---

## Engineering Rules

- No new files without justification
- No architecture changes without approval
- Avoid “nice-to-have” abstractions
- Prefer pure functions where possible
- Fail fast at the site level, not the batch level

---

## Context Reset Rule

Codex must not assume prior conversational context.

All decisions must be derived from:
- Repository files
- The current task brief

If ambiguity exists, Codex must stop and ask before proceeding.
