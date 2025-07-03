from pathlib import Path
from typing import List

class FileManager:
    """
    Handles file operations for audio input and transcript output.
    """

    def get_audio_files(self) -> List[Path] | None:
        """
        Scan the 'unprocessed/' folder for allowed audio/video files.
        Returns a sorted list of Path objects, or None if folder is missing.
        """
        allowed_exts = {'.mp3', '.mp4', '.wav', '.m4a'}
        unprocessed = Path(__file__).resolve().parent.parent / "unprocessed"

        if not unprocessed.exists() or not unprocessed.is_dir():
            print(f"[ERROR] Input folder does not exist: {unprocessed}")
            return None
        files = [f for f in unprocessed.iterdir() if f.suffix.lower() in allowed_exts and f.is_file()]
        return sorted(files)

    def save_transcript(self, input_path: Path, text: str):
        """
        Save the transcript as a .txt file in the 'processed/' folder with UTF-8 encoding.
        """
        processed = Path(__file__).resolve().parent.parent / "processed"
        processed.mkdir(exist_ok=True)
        out_name = input_path.stem + '.txt'
        out_path = processed / out_name
        with out_path.open('w', encoding='utf-8') as f:
            f.write(text)
        print(f"[DONE] Saved transcript: {out_path}")
