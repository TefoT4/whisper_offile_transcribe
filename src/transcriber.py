from pathlib import Path
from typing import Optional

class TranscriptionEngine:
    """
    Object-oriented wrapper for Whisper model transcription.
    """

    def __init__(self, model_name: str = "medium") -> None:
        """
        Initialize the engine with the specified Whisper model.
        """
        self.model_name = model_name
        self.model = None

    def load_model(self) -> None:
        """
        Loads the Whisper model if not already loaded.
        """
        if self.model is None:
            import whisper
            self.model = whisper.load_model(self.model_name)

    def transcribe(self, audio_path: Path) -> Optional[str]:
        """
        Transcribe an audio or video file to text.

        Args:
            audio_path (Path): Path to the audio or video file.

        Returns:
            Optional[str]: The transcribed text, or None if failed.
        """
        self.load_model()
        try:
            result = self.model.transcribe(str(audio_path))
            return result.get("text", "")
        except Exception:
            return None