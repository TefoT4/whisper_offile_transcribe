

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

def log(msg: str, level: str = "INFO"):
    print(f"[{level}] {msg}")

class TranscriptionEngine:
    """
    Object-oriented wrapper for Whisper model transcription.
    """

    def __init__(self, model_size: str = "tiny") -> None:
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
            log(f"[TranscriptionEngine] Failed to load Whisper model '{self.model_size}': {e}", level="ERROR")
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
            log("[TranscriptionEngine] Model not loaded. Cannot transcribe.", level="ERROR")
            return ""
        if not input_path.exists():
            log(f"[TranscriptionEngine] Input file does not exist: {input_path}", level="ERROR")
            return ""
        try:
            self.check_ffmpeg()
            result = self.model.transcribe(str(input_path))
            return result.get("text", "")
        except Exception as e:
            log(f"[TranscriptionEngine] Transcription failed: {e}", level="ERROR")
            return ""
    
    def check_ffmpeg(self):
        try:
            import subprocess
            subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            log("FFmpeg is available.", level="INFO")
        except Exception as e:
            log(f"FFmpeg not found or not in PATH. {e}", level="ERROR")