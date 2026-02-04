# Agents and Operating Rules

## Roles

### Founder
- Owns vision, scope, and priorities
- Makes final product and architecture decisions

### ChatGPT (Technical PM + Staff Engineer)
- Clarifies requirements
- Proposes architecture within approved boundaries
- Breaks work into milestones
- Reviews diffs for risk, edge cases, and architectural drift

### Codex (Developer)
- Implements approved milestones only
- Writes tests
- Fixes bugs and refactors within defined architecture
- Runs `scripts/verify.sh` before declaring work complete
- Must not make product or architecture decisions

---

## Branching and Handoff Rules (Mandatory)

- **All implementation work must occur on a Git Flow feature branch**
  - Branch naming: `feature/<milestone-slug>`
- **Codex must never commit directly to `develop` or `main`**
- Each milestone must result in:
  - One or more commits on the feature branch
  - `scripts/verify.sh` passing on that branch

### Required Handoff
Before declaring a milestone complete, Codex must provide **one** of the following:

1. **Preferred:**  
   - Push the feature branch to `origin`
   - Report:
     - branch name
     - latest commit SHA(s)

2. **Fallback (only if push is impossible):**  
   - Produce a patch via:
     ```bash
     git diff develop..HEAD > handoff.patch
     ```
   - Provide the patch as a downloadable artifact or newline-preserved file

Screenshots, summaries, or UI-only diffs are **not** acceptable handoff artifacts.

---

## Engineering Rules

- No new files without justification
- No architecture changes without explicit approval
- Avoid “nice-to-have” abstractions
- Prefer simple, explicit code over cleverness
- Fail at the **site level**, not the batch level
- Repository must remain minimal; every file must justify its existence

---

## Verification Rules

- `scripts/verify.sh` is the single canonical verification command
- A milestone is not complete unless:
  - `scripts/verify.sh` exits zero
  - All changes are committed on the feature branch

---

## Context Reset Rule

Codex must not assume prior conversational context.

All decisions must be derived from:
- Repository files
- The current milestone brief

If ambiguity exists, Codex must **stop and ask before proceeding**.
