from pathlib import Path
from typing import List

class FileManager:
    """
    Handles file operations for audio input and transcript output.
    """

    def get_audio_files(self) -> List[Path]:
        """
        Scan the 'unprocessed/' folder for allowed audio/video files.
        Returns a list of Path objects sorted alphabetically.
        """
        allowed_exts = {'.mp3', '.mp4', '.wav', '.m4a'}
        unprocessed = Path('unprocessed')
        if not unprocessed.exists():
            print(f"[ERROR] Input folder does not exist: {unprocessed}")
            return []
        files = [f for f in unprocessed.iterdir() if f.suffix.lower() in allowed_exts and f.is_file()]
        return sorted(files)

    def save_transcript(self, input_path: Path, text: str):
        """
        Save the transcript as a .txt file in the 'processed/' folder with UTF-8 encoding.
        """
        processed = Path('processed')
        processed.mkdir(exist_ok=True)
        out_name = input_path.stem + '.txt'
        out_path = processed / out_name
        with out_path.open('w', encoding='utf-8') as f:
            f.write(text)
        print(f"[DONE] Saved transcript: {out_path}")
