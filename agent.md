# 🤖 agent.md – Agent Instructions for Whisper Transcription Tool

This file contains all operational instructions for any coding agent (AI or human) tasked with contributing to the Whisper Transcription Tool. It serves as the **single source of truth** for initiating and guiding the build process.

---

## 🚀 Agent Startup Command

To begin executing the build plan, the developer will type:

```bash
start
```

Upon receiving this command, the agent must:

### 🛠️ Pre-Checklist Protocol (Run Once Per Feature)

The following steps **must be executed in strict order** before starting any work:

1. 🌿 **Create a new branch from `master`**:

   - Derive the branch name from the checklist item (e.g., `feature/transcription-engine`)
   - Execute:

     ```bash
     git checkout master
     git pull origin master
     git checkout -b feature/<item-name>
     ```

   - Do **not** proceed with file creation or package setup until the new branch is confirmed

2. 📦 **Ensure all required packages are identified**:

   - Determine which packages are needed for upcoming implementation
   - Create or update a `requirements.txt` file
   - Prompt the developer to run:

     ```bash
     pip install -r requirements.txt
     ```

   - Wait for the developer to confirm installation before proceeding

---

## 🔁 Build Execution Workflow

Once the pre-checklist protocol is complete:

1. 📚 Re-gather context from the following Markdown documents:

   - `agent.md` (this file)
   - `build.md`
   - `design_goals.md`
   - `README.md`

2. ✅ Confirm that context has been loaded

3. 📋 Read the first unchecked item in `build.md`

4. 🛠️ Begin implementing the item following all project conventions

5. 💬 Present code changes with a summary or diff

6. 👤 Say to the developer:

   > "Please test this. If you're happy, say `commit` and I will push."

7. ⛔ Wait for explicit developer approval

8. 💾 Once approved:

   - Propose a descriptive commit message
   - Commit the code
   - Push to the current `feature/...` branch
   - Mark the checklist item as completed

9. 🔁 Repeat this process for the next item

---

## 📐 Coding Philosophy (from design_goals.md)

- Follow OOP principles strictly: classes per concept, single responsibility
- Use Python 3.10+ features: type hints, docstrings, `pathlib.Path`
- Structure all code under `src/`
- Maintain an offline-first, CPU-compatible design (no cloud or GPU dependencies)
- Use `whisper-medium` by default unless instructed otherwise
- Default folders:

  - Input: `unprocessed/`
  - Output: `processed/`

---

## 🔧 Git and Workflow Rules

- All work must occur on a `feature/...` branch
- The developer will manually merge PRs into `master` via GitHub
- Use one branch per checklist item or feature
- Branch name conventions:

  - `feature/` for new features
  - `bugfix/` for fixes
  - `docs/` for documentation-only changes

---

## 📌 Agent Behavior Summary

| Task                  | Behavior                                                        |
| --------------------- | --------------------------------------------------------------- |
| Create Branch First   | Always start a new `feature/...` branch before any other action |
| Install Dependencies  | Add required packages to `requirements.txt` and ask for install |
| Gather Context        | Re-read `agent.md`, `build.md`, `design_goals.md`, `README.md`  |
| Execute Task          | Follow `build.md` checklist one item at a time                  |
| Show Result           | Present code summary or diff                                    |
| Wait for Confirmation | Ask developer to test and explicitly say `commit`               |
| Commit                | Propose message → Commit → Push to current feature branch       |
| Respect Boundaries    | Only use `src/`, `unprocessed/`, `processed/` folders           |

---

> This document enables the agent to operate in a fully guided, context-aware, test-driven coding loop — while enforcing quality and development discipline.
