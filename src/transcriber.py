
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

class TranscriptionEngine:
    """
    Object-oriented wrapper for Whisper model transcription.
    """

    def __init__(self, model_size: str = "medium") -> None:
        """
        Initialize the engine with the specified Whisper model.
        Loads the model and catches/report load-time errors.
        """
        self.model_size = model_size
        self.model = None
        try:
            import whisper
            self.model = whisper.load_model(self.model_size)
        except Exception as e:
            print(f"[TranscriptionEngine] Failed to load Whisper model '{self.model_size}': {e}")
            self.model = None

    def transcribe(self, audio_path: Path) -> Optional[str]:
        """
        Transcribe an audio or video file to text.

        Args:
            audio_path (Path): Path to the audio or video file.

        Returns:
            Optional[str]: The transcribed text, or None if failed.
        """
        if self.model is None:
            print("[TranscriptionEngine] Model not loaded. Cannot transcribe.")
            return None
        try:
            result = self.model.transcribe(str(audio_path))
            return result.get("text", "")
        except Exception:
            return None