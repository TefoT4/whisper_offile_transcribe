import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.file_manager import FileManager
from src.transcriber import TranscriptionEngine

if __name__ == "__main__":
    print("[INFO] Starting batch transcription...")

    fm = FileManager()

    # Allow user to select model size: tiny, base, or small (default: tiny)
    allowed_models = ["tiny", "base", "small"]

    model_size = "tiny"

    print(f"[INFO] Using Whisper model size: {model_size}")
    engine = TranscriptionEngine(model_size=model_size)

    files = fm.get_audio_files()
    if not files:
        print("[INFO] No audio/video files found in 'unprocessed/'. Exiting.")
        exit(0)

    processed_count = 0
    for f in files:
        print(f"[START] Transcribing: {f.name}")
        try:
            transcript = engine.transcribe(f)
            fm.save_transcript(f, transcript)
            print(f"[FINISH] Transcribed: {f.name}")
            processed_count += 1
        except Exception as e:
            print(f"[ERROR] Failed to transcribe {f.name}: {e}")

    print(f"[SUMMARY] Processed {processed_count} file(s). Done.")
