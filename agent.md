# 🤖 agent.md – Agent Instructions for Whisper Transcription Tool

This file contains all operational instructions for any coding agent (AI or human) tasked with contributing to the Whisper Transcription Tool. It serves as the **single source of truth** for initiating and guiding the build process.

---

## 🚀 Agent Startup Command

To begin executing the build plan, the developer will type:

```bash
start
```

Upon receiving this command, the agent must:

1. 📚 Re-gather context from the following Markdown documents:

   * `agent.md` (this file)
   * `build.md`
   * `design_goals.md`
   * `README.md`

2. ✅ Confirm that context has been loaded

3. 📋 Read the first unchecked item in `build.md`

4. 🛠️ Begin implementing the item following all project conventions

5. 💬 Present code changes with a summary or diff

6. 👤 Say to the developer:

   > "Please test this. If you're happy, say `commit` and I will push."

7. ⛔ Wait for explicit developer approval

8. 💾 Once approved:

   * Propose a descriptive commit message
   * Commit the code
   * Push to the current `feature/...` branch
   * Mark the checklist item as completed

9. 🔁 Repeat this process for the next item

---

## 📐 Coding Philosophy (from context\_guide.md & design\_goals.md)

* Follow OOP principles strictly: classes per concept, single responsibility
* Use Python 3.10+ features: type hints, docstrings, `pathlib.Path`
* Structure all code under `src/`
* Maintain an offline-first, CPU-compatible design (no cloud or GPU dependencies)
* Use `whisper-medium` by default unless instructed otherwise
* Default folders:

  * Input: `unprocessed/`
  * Output: `processed/`

---

## 🔧 Git and Workflow Rules (from git\_guide.md)

* All work must occur on a `feature/...` branch
* The developer will manually merge PRs into `master` via GitHub
* Use one branch per checklist item or feature
* Branch name conventions:

  * `feature/` for new features
  * `bugfix/` for fixes
  * `docs/` for documentation-only changes

---

## 📌 Agent Behavior Summary

| Task                  | Behavior                                                       |
| --------------------- | -------------------------------------------------------------- |
| Gather Context        | Re-read `agent.md`, `build.md`, `design_goals.md`, `README.md` |
| Execute Task          | Follow `build.md` checklist one item at a time                 |
| Show Result           | Present code summary or diff                                   |
| Wait for Confirmation | Ask developer to test and explicitly say `commit`              |
| Commit                | Propose message → Commit → Push to current feature branch      |
| Respect Boundaries    | Only use `src/`, `unprocessed/`, `processed/` folders          |

---

> This document replaces `context_guide.md` and incorporates relevant elements from `git_guide.md` and `product_information.md`. You may now delete these files from the workspace to reduce clutter and token usage. It ensures the agent remains modular, efficient, and human-directed in all phases of development.
