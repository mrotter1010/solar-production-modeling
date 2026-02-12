Milestone <N> — <Short Title>

============================================================
EXECUTION MODEL (APPLIES TO ALL BRANCHES)
============================================================

Roles
- Founder (You): owns scope/priorities, owns git-flow locally, applies Codex patch locally, runs final verification, commits/pushes to GitHub.
- ChatGPT: Technical PM + Staff Engineer; defines milestone brief/architecture; reviews diffs.
- Codex: Developer; edits only allowed files; produces unified diff patch at handoff; does NOT push to GitHub; does NOT do git-flow; does NOT rewrite history.

Operating constraints (Codex sandbox)
- No GitHub network access
- Cannot delete .git
- Cannot hard reset branches
- Cannot rewrite history
Therefore:
- Codex edits in place and hands off via “git diff” patch only.
- Local repo is the only canonical git history.

============================================================
GIT-FLOW DISCIPLINE
============================================================

All official branching + merging happens locally via git-flow (Founder only).

Start Milestone (Founder runs locally)
- git checkout develop
- git pull origin develop
- git flow feature start <milestone-slug>
- git push -u origin feature/<milestone-slug>

Complete Milestone (Founder runs locally)
- save Codex diff as <milestone-output.patch>
- git apply --3way <milestone-output.patch>
- scripts/verify.sh
- git add -A
- git commit -m "Milestone <N>: <Short Title>"
- git push
- git flow feature finish <milestone-slug>
- git push origin develop

Codex must NOT
- create or finish git-flow branches
- push to GitHub
- merge branches
- provide commit SHAs as a handoff artifact

============================================================
REQUIRED ACK CHECKPOINTS (CODEX MUST FOLLOW)
============================================================

ACK 1 — Preflight (before any code changes)
Codex runs:
- ls -la
- git status -sb
- git diff --name-only
Codex replies exactly:
ACK — Preflight complete. Ready for milestone brief.

ACK 2 — Scope Lock (after receiving milestone brief)
Codex replies exactly:
ACK — Scope understood. Implementing only allowed files and respecting out-of-scope constraints.

ACK 3 — Handoff Complete (end of milestone)
Codex must provide, in order:
1) scripts/verify.sh output summary (must exit 0)
2) git diff --name-only
3) git status -sb
4) FULL unified diff (git diff output pasted in chat)
Codex ends exactly:
ACK — Milestone implementation complete. Patch provided.

Handoff format rules
- The ONLY accepted handoff artifact is the full unified diff (git diff output).
- No screenshots. No partial diffs. No summaries in place of the diff.

============================================================
OBJECTIVE
============================================================

<Describe the single concrete outcome this milestone must deliver.>

============================================================
SCOPE (IN)
============================================================

- <bullet>
- <bullet>

============================================================
OUT OF SCOPE
============================================================

- <bullet>
- <bullet>

============================================================
INPUTS
============================================================

- <input description>
- <formats / required fields / assumptions>
- If no new inputs: “No new inputs introduced.”

============================================================
OUTPUTS
============================================================

- <output description>
- <directory layout / filenames>
- Runtime outputs (e.g., under data/) must not be committed unless explicitly approved.

============================================================
FILES TO CREATE OR MODIFY (ALLOWLIST)
============================================================

Codex may ONLY create/modify the following paths/files:
- <path or file>
- <path or file>

Anything not listed here must not be changed. If additional files are required, Codex must stop and request approval.

============================================================
ACCEPTANCE CRITERIA
============================================================

All must be true:
- <deterministic statement>
- <deterministic statement>
- scripts/verify.sh exits 0
- no forbidden files modified

============================================================
VERIFICATION REQUIREMENTS
============================================================

- Required unit tests: <list>
- Required smoke checks: <list>
- Required commands beyond scripts/verify.sh: <list or “None”>
Final authority is local verification on Founder machine.

============================================================
NOTES / OPEN QUESTIONS
============================================================

None.
(or list items)

============================================================
APPROVAL GATE
============================================================

Milestone is complete only after:
- acceptance criteria are met
- patch-based handoff is provided (full git diff)
- local verification passes
- changes are reviewed/approved by ChatGPT
- feature branch is finished via git-flow
