
from pathlib import Path
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

    def transcribe(self, input_path: Path) -> str:
        """
        Transcribe an audio or video file to text.

        Args:
            input_path (Path): Path to the audio or video file.

        Returns:
            str: The transcribed text, or an empty string if failed.
        """
        if self.model is None:
            print("[TranscriptionEngine] Model not loaded. Cannot transcribe.")
            return ""
        if not input_path.exists():
            print(f"[TranscriptionEngine] Input file does not exist: {input_path}")
            return ""
        try:
            self.check_ffmpeg()
            result = self.model.transcribe(str(input_path))
            return result.get("text", "")
        except Exception as e:
            print(f"[TranscriptionEngine] Transcription failed: {e}")
            return ""
    
    def check_ffmpeg(self):
        try:
            import subprocess
            subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("[INFO] FFmpeg is available.")
        except Exception as e:
            print("[ERROR] FFmpeg not found or not in PATH.", e)