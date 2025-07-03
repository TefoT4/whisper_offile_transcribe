# 🎧 Whisper-Based Offline Transcription Tool

## 📝 Overview

This project is a Python-based offline transcription tool built around OpenAI’s [`whisper-large-v3`](https://huggingface.co/openai/whisper-large-v3) automatic speech recognition (ASR) model. It converts audio and video content into high-quality text transcriptions without relying on any cloud service — ensuring privacy, full control, and offline performance.

Designed using **object-oriented software architecture**, this tool is ideal for developers with C# or Java backgrounds who prefer structured, maintainable code.

It is intended for:

* Researchers and educators working with recorded interviews or lectures
* Media producers managing large libraries of audio/video content
* Developers and data scientists who want to integrate ASR into workflows
* Anyone needing fast, offline transcription without exposing sensitive data

---

## 🧱 Features

* 🔍 Transcribe `.mp4`, `.mp3`, `.wav`, and more using `whisper-medium` (default)
* 📂 Scan all files in an `unprocessed/` folder
* 📄 Output `.txt` files to a `processed/` folder with matching filenames
* 🔧 OOP design: easily extensible with future features (e.g., SRT, language override)
* 💡 Simple but professional folder layout and script interface

---

## 📁 Folder Structure

```plaintext
J:\repos\huggingface_transcribe\
├── env\                         # Python virtual environment
├── src\                         # Source code modules
│   ├── transcribe.py            # CLI entry point
│   ├── transcriber.py           # TranscriptionEngine class
│   └── file_manager.py          # FileManager class
├── unprocessed\                 # Drop files here for transcription
├── processed\                   # Output transcripts
├── README.md                    # Project overview and usage
├── agent.md                     # Agent behavior and workflow rules
├── design_goals.md              # Software architecture principles
└── build.md                     # Development checklist
```

---

## 🔄 How It Works

### 🔁 Workflow Summary

1. **Place input files** in the `unprocessed/` folder:

   * Supported formats: `.mp4`, `.mp3`, `.wav`, `.m4a`, etc.

2. **Run the transcription script** from the `src/` directory:

   ```bash
   python src/transcribe.py
   ```

3. The script:

   * Loads the `whisper-medium` model by default
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

From your project root folder:

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

* **Input folder**: `unprocessed/`
* **Output folder**: `processed/`
* **Model**: `"medium"` by default; switchable via future config or CLI

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

---

> This `README.md` now reflects the streamlined planning structure. All relevant implementation context is consolidated in `agent.md`, `build.md`, and `design_goals.md`.
