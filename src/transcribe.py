
import sys
import argparse
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.file_manager import FileManager
from src.transcriber import TranscriptionEngine

if __name__ == "__main__":
    print("[INFO] Starting batch transcription...")

    parser = argparse.ArgumentParser(description="Batch transcribe audio/video files using Whisper.")
    parser.add_argument(
        "--model",
        type=str,
        default="tiny",
        help="Whisper model size: tiny, base, small, medium, large-v3 (default: medium)"
    )
    args = parser.parse_args()

    allowed_models = ["tiny", "base", "small"]
    model_size = args.model.lower()
    if model_size not in allowed_models:
        print(f"[WARN] Invalid model '{model_size}' specified. Falling back to 'medium'.")
        model_size = "medium"

    print(f"[INFO] Using Whisper model size: {model_size}")
    engine = TranscriptionEngine(model_size=model_size)

    fm = FileManager()
    
    files = fm.get_audio_files()
    
    if files is None:
        print("[ABORT] Cannot continue without input folder.")
        exit(1)
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
