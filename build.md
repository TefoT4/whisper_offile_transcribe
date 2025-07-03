# 🛠️ BUILD.md – Feature Development Checklist for Coding Agent

This document is a live **vibe-coding tracker** and checklist. It guides coding agents through the step-by-step implementation of the Whisper Transcription Tool, aligned with the context and standards defined in `agent.md`.

⚠️ **Important Note:** During setup, all Whisper model files (e.g., `medium.pt`) must be downloaded to a controlled directory. The developer's preferred cache path is:

```bash
set WHISPER_CACHE=E:\whisper-cache
```

The agent must ensure that this environment variable is set prior to any model download to avoid writing to the default location (`~/.cache/whisper`).

---

## 🔗 Related Documents

* [`agent.md`](./agent.md) – Central context and behavior guide
* [`README.md`](./README.md) – Project summary and usage
* [`design_goals.md`](./design_goals.md) – Software design principles

---

## ✅ Build Checklist

### 🎯 Phase 1 – Core System Implementation

#### `feature/transcription-engine`

* [x] Create `src/transcriber.py`
* [x] Define `TranscriptionEngine` class

  * [ ] Add `__init__(self, model_size: str = "medium")`

    * [ ] Load Whisper model using `whisper.load_model(...)`
    * [ ] Catch and report load-time errors
  * [ ] Add `transcribe(self, input_path: Path) -> str`

    * [ ] Validate input file exists
    * [ ] Run `model.transcribe()`
    * [ ] Return plain string transcript
* [ ] Manually test transcription of `.mp4` and `.wav` files
* [ ] Ensure model runs with **CPU-only**, no GPU assumptions
* [ ] Ensure model is downloaded into `E:\whisper-cache` by setting the `WHISPER_CACHE` env variable

#### `feature/file-manager`

* [ ] Create `src/file_manager.py`
* [ ] Define `FileManager` class

  * [ ] Method: `get_audio_files(self) -> List[Path]`

    * [ ] Scan `unprocessed/` for allowed extensions: `.mp4`, `.mp3`, `.wav`, `.m4a`
    * [ ] Return `Path` list sorted alphabetically
  * [ ] Method: `save_transcript(self, input_path: Path, text: str)`

    * [ ] Convert filename to `.txt`
    * [ ] Save to `processed/` folder with UTF-8 encoding
* [ ] Validate folder existence and permissions
* [ ] Manually test with at least two dummy input files

#### `feature/cli-runner`

* [ ] Create `src/transcribe.py`
* [ ] Set up script as `if __name__ == "__main__":`
* [ ] Instantiate `FileManager` and `TranscriptionEngine`
* [ ] Retrieve files from `unprocessed/`
* [ ] Transcribe each file
* [ ] Save transcripts to `processed/`
* [ ] Print status for each file (started, finished, saved)
* [ ] Print summary count of files processed

---

### 🔧 Phase 2 – Enhancements & Quality

#### `feature/model-selection`

* [ ] Accept `--model` as CLI argument

  * [ ] Validate against supported models: `tiny`, `base`, `small`, `medium`, `large-v3`
* [ ] Pass user selection to `TranscriptionEngine`
* [ ] Provide fallback to `medium` on invalid input

#### `feature/logging-support`

* [ ] Add simple logging using `print()` with `[INFO]`, `[ERROR]`, `[DONE]` tags
* [ ] Replace raw `print()` with wrapper logging function
* [ ] Optionally swap in Python `logging` module with INFO/WARNING/ERROR levels

#### `feature/unit-tests`

* [ ] Create a `tests/` directory
* [ ] Test `TranscriptionEngine.transcribe()` with stubbed audio file
* [ ] Test `FileManager.get_audio_files()` with test folder
* [ ] Test `FileManager.save_transcript()` writes correct output
* [ ] Use `unittest` or `pytest`

---

### 📝 Phase 3 – Documentation & Maintenance

#### `feature/readme-docs`

* [ ] Ensure all documents reflect current implementation:

  * [ ] `README.md`
  * [ ] `agent.md`
  * [ ] `design_goals.md`
  * [ ] `build.md`

#### `feature/error-handling`

* [ ] Catch unsupported file types
* [ ] Handle missing or unreadable input files
* [ ] Catch exceptions in `model.transcribe()` and continue to next file
* [ ] Report meaningful error messages without crashing

---

## 📌 Agent Rules (From `agent.md`)

* All source files go under `src/`
* Default model is `medium`
* No GPU or cloud dependencies allowed
* Always log file-level progress clearly
* Use pathlib’s `Path` and type annotations
* Whisper models must be cached in `E:\whisper-cache` using the `WHISPER_CACHE` environment variable

---

> This document is part of a lean, high-efficiency planning stack: `agent.md`, `build.md`, `design_goals.md`, and `README.md`.
