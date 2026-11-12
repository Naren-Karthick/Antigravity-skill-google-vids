#!/usr/bin/env python3
"""Report audio duration using ffprobe when available, otherwise WAV metadata."""

import argparse
import json
import shutil
import subprocess
import wave
from pathlib import Path


def duration_with_ffprobe(path: Path) -> float:
    executable = shutil.which("ffprobe")
    if not executable:
        raise RuntimeError("ffprobe is not installed")
    result = subprocess.run(
        [executable, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(result.stdout.strip())


def duration_with_wave(path: Path) -> float:
    with wave.open(str(path), "rb") as audio:
        frames, rate = audio.getnframes(), audio.getframerate()
        if rate <= 0:
            raise ValueError("Invalid WAV sample rate")
        return frames / rate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio_file", type=Path)
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()
    path = args.audio_file

    if not path.is_file():
        parser.error(f"File does not exist: {path}")

    try:
        try:
            seconds = duration_with_ffprobe(path)
            method = "ffprobe"
        except (RuntimeError, subprocess.CalledProcessError, ValueError):
            if path.suffix.lower() != ".wav":
                raise RuntimeError("ffprobe is required for this format; WAV fallback is unavailable")
            seconds = duration_with_wave(path)
            method = "wave"
        if seconds <= 0:
            raise ValueError("Audio duration is not positive")
    except Exception as exc:
        parser.exit(2, f"Error: {exc}\n")

    if args.json:
        print(json.dumps({"file": str(path), "duration_seconds": round(seconds, 3), "method": method}))
    else:
        print(f"{seconds:.3f} seconds ({seconds / 60:.2f} minutes) [{method}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
