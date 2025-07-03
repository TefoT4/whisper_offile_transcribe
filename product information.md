# 🏋️️ Product Information: Whisper-Based Transcription Tool

## 📅 Project Title

**Whisper-Based Offline Transcription Tool**

## 🛠️ Purpose

To create a reliable, privacy-respecting transcription tool that runs entirely offline using OpenAI's `whisper-large-v3` model. The tool is designed to convert audio/video files into text using a folder-based workflow, ensuring high-quality speech-to-text conversion for researchers, educators, media professionals, and developers.

## 🌐 Target Users

* Researchers working with interviews or field recordings
* Educators and archivists converting lectures and oral histories
* Developers and data engineers needing reproducible offline transcriptions
* Privacy-conscious users seeking cloud-free solutions

## 🚀 Objectives

* Enable accurate offline transcription from audio/video files
* Preserve privacy by avoiding cloud processing
* Provide a clean, OOP-based Python architecture for easy maintenance and extension
* Automate batch processing through folder scanning and predictable output

## 📊 Key Features

* Uses OpenAI's state-of-the-art `whisper-large-v3` model for transcription
* CLI script automatically scans an `unprocessed/` folder for media files
* Saves output to a `processed/` folder with matching `.txt` filenames
* Written in modern Python with type-safe, modular design
* Easily testable and extendable architecture

## 🔄 Core Workflow Summary

1. User places media files in `unprocessed/`
2. Script scans the folder and loads Whisper model once
3. Each file is transcribed and output to `processed/` as a `.txt` file
4. Resulting transcripts are ready for review, archive, or downstream use

## ⚖️ Design Philosophy

* **Modularity**: Each component (I/O, transcription) is encapsulated
* **Simplicity**: Avoid unnecessary abstraction or complexity
* **Transparency**: Log all steps and errors clearly for the user
* **Reusability**: Classes are built with testing and reuse in mind
* **Scalability**: Architecture supports easy expansion to SRTs, UI, etc.

## 🌐 Language and Platform

* Written in Python 3.10+
* Designed for Windows 10+ with limited C: drive storage
* Folder paths configurable to user-specified drives (e.g., `E:\`, `J:\`)

## 💼 License

Apache 2.0 (inherits from Whisper)

## 📓 Documentation

* `README.md`: Project overview and usage
* `DESIGN_GOALS.md`: Architectural and design intentions
* Code modules: `transcribe.py`, `transcriber.py`, `file_manager.py`

## 📢 Future Scope

* Subtitle export (.srt/.vtt)
* Multi-language support
* Speaker diarization
* Web UI or GUI extension
* Config file / CLI argument parsing
