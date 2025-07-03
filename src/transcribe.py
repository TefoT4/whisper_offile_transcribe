
import sys
import argparse
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.file_manager import FileManager
from src.transcriber import TranscriptionEngine

def log(msg: str, level: str = "INFO"):
    print(f"[{level}] {msg}")

if __name__ == "__main__":
    log("Starting batch transcription...", level="INFO")

    parser = argparse.ArgumentParser(description="Batch transcribe audio/video files using Whisper.")
    parser.add_argument(
        "--model",
        type=str,
        default="tiny",
        help="Whisper model size: tiny, base, small, medium, large-v3 (default: medium)"
    )
    args = parser.parse_args()

    allowed_models = ["tiny", "base", "small", "medium", "large-v3"]
    model_size = args.model.lower()
    if model_size not in allowed_models:
        log(f"Invalid model '{model_size}' specified. Falling back to 'medium'.", level="WARN")
        model_size = "medium"

    log(f"Using Whisper model size: {model_size}", level="INFO")
    engine = TranscriptionEngine(model_size=model_size)

    fm = FileManager()
    files = fm.get_audio_files()

    if files is None:
        log("Cannot continue without input folder.", level="ABORT")
        exit(1)
    if not files:
        log("No audio/video files found in 'unprocessed/'. Exiting.", level="INFO")
        exit(0)

    processed_count = 0
    for f in files:
        log(f"Transcribing: {f.name}", level="START")
        try:
            transcript = engine.transcribe(f)
            fm.save_transcript(f, transcript)
            log(f"Transcribed: {f.name}", level="FINISH")
            processed_count += 1
        except Exception as e:
            log(f"Failed to transcribe {f.name}: {e}", level="ERROR")

    log(f"Processed {processed_count} file(s). Done.", level="SUMMARY")
