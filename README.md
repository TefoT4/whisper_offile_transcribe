# 🎷 Whisper-Based Offline Transcription Tool

## 📝 Overview

This project is a Python-based offline transcription tool built around OpenAI’s [`whisper-large-v3`](https://huggingface.co/openai/whisper-large-v3) automatic speech recognition (ASR) model. It converts audio and video content into high-quality text transcriptions without relying on any cloud service — ensuring privacy, full control, and offline performance.

Designed using **object-oriented software architecture**, this tool is ideal for developers with C# or Java backgrounds who prefer structured, maintainable code.

---

## 🌟 Purpose

This tool solves the need for a **private, automated, offline transcription system**. It supports a clean CLI interface, folder-based input/output, and extensible modules for future upgrades.

---

## 🧱 Features

* 🔍 Transcribe `.mp4`, `.mp3`, `.wav`, and more using `whisper-large-v3`
* 📂 Scan all files in an `unprocessed/` folder
* 📄 Output `.txt` files to a `processed/` folder with matching filenames
* 🔧 OOP design: easily extensible with future features (e.g., SRT, language override)
* 💡 Simple but professional folder layout and script interface

---

## 📁 Folder Structure

```plaintext
J:\repos\huggingface_transcribe\
├── env\                         # Python virtual environment
├── transcribe.py                # CLI entry point (main script)
├── transcriber.py               # TranscriptionEngine class
├── file_manager.py              # FileManager class
├── unprocessed\                 # Drop files here for transcription
│   ├── myvideo.mp4
│   └── meeting.wav
├── processed\                   # Output transcripts
│   ├── myvideo.txt
│   └── meeting.txt
├── README.md                    # Project overview and instructions
└── DESIGN_GOALS.md              # Software design rationale
```

---

## 🔄 How It Works

### 🔁 Workflow Summary

1. **Place input files** in the `unprocessed/` folder:

   * Supported formats: `.mp4`, `.mp3`, `.wav`, `.m4a`, etc.

2. **Run the transcription script** from the root directory:

   ```bash
   python transcribe.py
   ```

3. The script:

   * Loads the `whisper-large-v3` model once
   * Transcribes every media file in the `unprocessed/` folder
   * Saves each transcript to `processed/` with the same base filename and a `.txt` extension

4. **Result**:

   * Human-readable `.txt` transcripts are available in the `processed/` folder
   * You can archive, edit, or further analyze them as needed

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python **3.10 or higher**
* FFmpeg installed and available in PATH
* `pip` (Python package manager)
* Optional: install Python to `E:\` if you're low on `C:\` space

### 📦 Install Dependencies

From your working folder:

```bash
cd J:\repos\huggingface_transcribe
python -m venv env
.\env\Scripts\activate         # PowerShell
# OR
env\Scripts\activate.bat      # Command Prompt

pip install git+https://github.com/openai/whisper.git
pip install ffmpeg-python
```

---

## ⚙️ Configuration

Currently hardcoded values (can be refactored later):

* **Input folder**: `unprocessed/`
* **Output folder**: `processed/`
* **Model**: `"large-v3"` (You may switch to `"medium"` or `"small"` for lower RAM)

Planned support for:

* Language override
* Config files or CLI flags

---

## 🧠 Future Enhancements

| Feature                                     | Status     |
| ------------------------------------------- | ---------- |
| `.srt` or `.vtt` subtitle export            | 🔜 Planned |
| Language override support                   | 🔜 Planned |
| Speaker diarization                         | 🔜 Planned |
| Progress bar or logging system              | 🔜 Planned |
| Batch resumption (skipping processed files) | 🔜 Planned |
| Simple GUI or web interface                 | 🔜 Planned |

---

## 💡 Philosophy

This is not just a one-off script — it's a modular, thoughtfully structured tool. Built with OOP principles to support:

* Unit testing
* Reusability
* Easy onboarding for new developers

> “Build it as if you're handing it off to your future self as a teammate.”

---

## 🔐 License

This tool uses the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
The Whisper model is provided by [OpenAI](https://github.com/openai/whisper), also under Apache 2.0.

---

## 🙌 Credits

* [OpenAI Whisper](https://github.com/openai/whisper) – automatic speech recognition
* [Hugging Face](https://huggingface.co/openai/whisper-large-v3) – model hosting
* FFmpeg – audio preprocessing
* Python community – tools and ecosystem
