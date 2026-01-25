# Phase 1: Video → Audio  → Transcript
import os
from moviepy import VideoFileClip
import whisper

# Folders
VIDEO_DIR = "videos"
AUDIO_DIR = "audio"
TRANSCRIPT_DIR = "transcripts"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

# Load Whisper model (use 'base' for balance)
model = whisper.load_model("base")


def video_to_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()


def audio_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]


def process_videos():
    for file in os.listdir(VIDEO_DIR):
        if file.endswith(".mp4"):
            video_path = os.path.join(VIDEO_DIR, file)

            audio_name = file.replace(".mp4", ".mp3")
            audio_path = os.path.join(AUDIO_DIR, audio_name)

            text_name = file.replace(".mp4", ".txt")
            transcript_path = os.path.join(TRANSCRIPT_DIR, text_name)

            print(f"Processing video: {file}")

            # Step 1: Video → Audio
            video_to_audio(video_path, audio_path)

            # Step 2: Audio → Text
            text = audio_to_text(audio_path)

            # Step 3: Save transcript
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Transcript saved: {transcript_path}\n")


if __name__ == "__main__":
    process_videos()

