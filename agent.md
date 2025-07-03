# 🤖 agent.md – Agent Instructions for Whisper Transcription Tool

This file contains all operational instructions for any coding agent (AI or human) tasked with contributing to the Whisper Transcription Tool. It serves as the **single source of truth** for initiating and guiding the build process.

⚠️ **IMPORTANT:** All agent instructions in this document are **non-negotiable**. You must adhere to them exactly. No deviations, assumptions, or shortcuts are permitted. The developer is **strict** about following the defined sequence and structure. Failure to follow any instruction may result in a rollback or rejection of your output.

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

   * Derive the branch name from the checklist item (e.g., `feature/transcription-engine`)
   * Execute:

     ```bash
     git checkout master
     git pull origin master
     git checkout -b feature/<item-name>
     ```
   * Do **not** proceed with file creation or package setup until the new branch is confirmed

2. 📦 **Ensure all required packages are identified**:

   * Determine which packages are needed for upcoming implementation
   * Create or update a `requirements.txt` file
   * ✅ Use the correct dependency for OpenAI Whisper:

     ```txt
     git+https://github.com/openai/whisper.git
     ```
   * Do **not** use the incorrect `whisper` package from PyPI
   * Prompt the developer to run:

     ```bash
     pip install -r requirements.txt
     ```
   * Wait for the developer to confirm installation before proceeding

3. 🗂️ **Set up Whisper model cache directory via .env file**:

   * Ensure the project root contains a `.env` file with:

     ```env
     WHISPER_CACHE=E:\whisper-cache
     ```
   * Add `python-dotenv` to `requirements.txt`
   * Ensure `transcriber.py` includes:

     ```python
     from dotenv import load_dotenv
     load_dotenv()
     ```
   * Confirm that the model will download into `E:\whisper-cache` on first use

---

## 🔁 Build Execution Workflow

Once the pre-checklist protocol is complete:

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

## 📐 Coding Philosophy (from design\_goals.md)

* Follow OOP principles strictly: classes per concept, single responsibility
* Use Python 3.10+ features: type hints, docstrings, `pathlib.Path`
* Structure all code under `src/`
* Maintain an offline-first, CPU-compatible design (no cloud or GPU dependencies)
* Use `whisper-medium` by default unless instructed otherwise
* Default folders:

  * Input: `unprocessed/`
  * Output: `processed/`

---

## 🔧 Git and Workflow Rules

* All work must occur on a `feature/...` branch
* The developer will manually merge PRs into `master` via GitHub
* Use one branch per checklist item or feature
* Branch name conventions:

  * `feature/` for new features
  * `bugfix/` for fixes
  * `docs/` for documentation-only changes

---

## 📌 Agent Behavior Summary

| Task                     | Behavior                                                        |
| ------------------------ | --------------------------------------------------------------- |
| Create Branch First      | Always start a new `feature/...` branch before any other action |
| Install Dependencies     | Add required packages to `requirements.txt` and ask for install |
| Use Correct Whisper      | Must use `git+https://github.com/openai/whisper.git` only       |
| Load from .env           | Ensure `.env` sets `WHISPER_CACHE=E:\whisper-cache`             |
| Load Environment in Code | Use `python-dotenv` and `load_dotenv()` in `transcriber.py`     |
| Gather Context           | Re-read `agent.md`, `build.md`, `design_goals.md`, `README.md`  |
| Execute Task             | Follow `build.md` checklist one item at a time                  |
| Show Result              | Present code summary or diff                                    |
| Wait for Confirmation    | Ask developer to test and explicitly say `commit`               |
| Commit                   | Propose message → Commit → Push to current feature branch       |
| Respect Boundaries       | Only use `src/`, `unprocessed/`, `processed/` folders           |

---

> 🔒 **This document is the source of truth. Follow every instruction exactly.**
> The developer is very strict about process compliance. No steps may be skipped or reordered.
> Always confirm before proceeding to the next phase.
