#!/usr/bin/env python3
"""Validate basic media file presence and, when available, ffprobe metadata."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media_file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    path = args.media_file

    report = {
        "file": str(path),
        "exists": path.is_file(),
        "size_bytes": path.stat().st_size if path.is_file() else 0,
        "extension": path.suffix.lower(),
        "ffprobe_available": shutil.which("ffprobe") is not None,
        "probe": None,
        "errors": [],
    }
    if not report["exists"]:
        report["errors"].append("File does not exist")
    elif report["size_bytes"] == 0:
        report["errors"].append("File is empty")

    ffprobe = shutil.which("ffprobe")
    if report["exists"] and report["size_bytes"] > 0 and ffprobe:
        command = [
            ffprobe, "-v", "error", "-show_entries",
            "format=duration,format_name:stream=codec_type,codec_name,width,height",
            "-of", "json", str(path),
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            report["errors"].append(result.stderr.strip() or "ffprobe failed")
        else:
            try:
                report["probe"] = json.loads(result.stdout)
            except json.JSONDecodeError as exc:
                report["errors"].append(f"Could not parse ffprobe output: {exc}")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"File: {report['file']}")
        print(f"Exists: {report['exists']} | Size: {report['size_bytes']} bytes")
        if report["probe"]:
            print(json.dumps(report["probe"], indent=2))
        for error in report["errors"]:
            print(f"ERROR: {error}")
        if not ffprobe and report["exists"]:
            print("NOTE: ffprobe unavailable; codec, duration, and dimensions were not verified.")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
