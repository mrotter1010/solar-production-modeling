# Milestone <N> — <Short Title>

## Branching + Handoff (Required)

- Create and work on: `feature/<milestone-slug>`
- Do **not** commit directly to `develop` or `main`

Before declaring this milestone complete, Codex must:
1. Run `scripts/verify.sh` and confirm it exits zero
2. Commit all changes on the feature branch
3. Push the feature branch to `origin`
4. Report:
   - branch name
   - latest commit SHA(s)

Screenshots or UI-only diffs are **not** acceptable as a handoff.

---

## Objective

Describe the **single, concrete outcome** this milestone must deliver.
Focus on capability, not implementation details.

Example:
> Enable batch processing of site inputs and deterministic output generation.

---

## Scope (In)

Explicitly list what **is included** in this milestone.

- Bullet points only
- Be precise
- Assume Codex will implement *exactly* what is written here

---

## Out of Scope

Explicitly list what **must not** be implemented in this milestone.

- This section is mandatory
- Use it to prevent scope creep
- If something is “later,” say so

---

## Inputs

Describe required inputs, formats, or assumptions.

- File formats
- Required columns or fields
- Expected conventions

If no new inputs are introduced, say so explicitly.

---

## Outputs

Describe required outputs and structure.

- Directory layout
- File naming conventions
- Required artifacts for traceability or reproducibility

---

## Files to Create or Modify

Explicit list of files Codex is allowed to touch.

- New files
- Existing files that may be modified

Anything not listed here must not be changed.

---

## Acceptance Criteria

Verifiable conditions that must all be true for approval.

- Deterministic, testable statements
- Prefer filesystem assertions and command exit codes
- Avoid subjective language

Example:
- `scripts/verify.sh` exits zero
- All required outputs are created
- Errors are isolated to site level
- Tests pass

---

## Verification Requirements

How correctness is proven.

- Required tests
- Required smoke checks
- Required commands (if any beyond `scripts/verify.sh`)

If nothing beyond `scripts/verify.sh` is required, state that explicitly.

---

## Notes / Open Questions

Anything that:
- requires clarification
- represents a known tradeoff
- is intentionally deferred

If empty, write: `None`.

---

## Approval Gate

This milestone is considered complete **only after**:
- Acceptance criteria are met
- Handoff requirements are satisfied
- Changes are reviewed and approved by ChatGPT
