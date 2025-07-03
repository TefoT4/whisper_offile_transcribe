# 💪 Design Goals – Whisper-Based Transcription Tool

## 🌟 Overview

This document outlines the guiding principles and architectural intent for building the Whisper-based offline transcription tool. The software is designed with **clarity**, **modularity**, and **long-term maintainability** in mind. It leverages principles familiar to developers with object-oriented backgrounds, particularly from languages like C#.

---

## 🔢 High-Level Software Goals

| Goal                       | Description                                                                |
| -------------------------- | -------------------------------------------------------------------------- |
| **Modularity**             | Separate components into clean, logical classes and modules                |
| **Separation of Concerns** | Each component should handle only its specific responsibility              |
| **Abstraction**            | Wrap external dependencies and logic behind high-level interfaces          |
| **Encapsulation**          | Expose clean APIs while hiding implementation details                      |
| **Extensibility**          | Design so new features (e.g., SRT export) can be added with minimal change |
| **Readability**            | Prioritize clear, understandable code for human readers                    |
| **Robustness**             | Include basic error handling, validations, and fallback logic              |
| **Testability**            | Make classes and methods easy to test in isolation                         |

---

## 🔧 Component Responsibilities

| Component             | Responsibilities                                                  |
| --------------------- | ----------------------------------------------------------------- |
| `transcribe.py`       | Entry-point CLI script; coordinates I/O and model processing      |
| `TranscriptionEngine` | Load and manage the Whisper model; provide `.transcribe()` method |
| `FileManager`         | List files in `unprocessed/`, save `.txt` outputs in `processed/` |
| _(Future)_ `Logger`   | Centralize status messages and error reporting                    |
| _(Future)_ `Config`   | Store user-defined settings (paths, model size, language, etc.)   |

---

## 📁 Folder Layout for Code & Data

```plaintext
J:\repos\huggingface_transcribe\
├── env\                         # Python virtual environment
├── src\                         # Source code modules
│   ├── transcribe.py            # Main script / CLI runner
│   ├── transcriber.py           # TranscriptionEngine class
│   └── file_manager.py          # FileManager class
├── unprocessed\                 # Input files
├── processed\                   # Output transcripts
├── README.md                    # Project overview
├── agent.md                     # Agent rules and behavior
└── build.md                     # Implementation checklist
```

---

## 🔄 Development Style

- Python 3.10+ with type hints and docstrings
- One class per concept
- Avoid monolithic scripts; encapsulate logic cleanly
- Avoid magic strings or side effects in modules

---

## ✨ Extensibility Targets

| Feature                        | Design Readiness                                  |
| ------------------------------ | ------------------------------------------------- |
| Subtitle (.srt) export         | ✅ Cleanly pluggable in `TranscriptionEngine`     |
| GUI interface (Tkinter/web)    | ✅ Logic is decoupled from CLI                    |
| Model configuration            | ✅ Can be injected via constructor or config file |
| Language override              | ✅ Add as method param or CLI flag                |
| Batch tracking / checkpointing | ✅ File naming and state checks supported         |

---

## 🚀 Testing Considerations

- `TranscriptionEngine.transcribe()` returns raw text
- `FileManager.get_audio_files()` returns a list of `Path` objects
- File output is deterministic and can be verified line-by-line
- Unit testing can isolate audio, transcription, and file handling independently

---

## ✅ Summary

This project adheres to a professional software development standard, translating C#/Java OOP design principles into Python. Each class, function, and folder serves a clear role, allowing the tool to grow without sacrificing maintainability or reliability.

🔄 This document is part of a lean planning stack with `agent.md`, `build.md`, and `README.md`. Other documents have been retired and merged for clarity.
