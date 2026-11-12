#!/usr/bin/env python3
"""Check an exported video exists, is non-empty, and matches optional expectations."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video_file", type=Path)
    parser.add_argument("--expected-width", type=int)
    parser.add_argument("--expected-height", type=int)
    parser.add_argument("--min-duration", type=float, default=0.1)
    parser.add_argument("--max-duration", type=float)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    path = args.video_file

    report = {
        "file": str(path),
        "exists": path.is_file(),
        "size_bytes": path.stat().st_size if path.is_file() else 0,
        "duration_seconds": None,
        "width": None,
        "height": None,
        "video_stream_found": False,
        "playback_verified": False,
        "errors": [],
        "notes": [],
    }

    if not report["exists"]:
        report["errors"].append("Export file does not exist")
    elif report["size_bytes"] <= 0:
        report["errors"].append("Export file is empty")

    ffprobe = shutil.which("ffprobe")
    if report["exists"] and report["size_bytes"] > 0:
        if not ffprobe:
            report["notes"].append("ffprobe unavailable; duration and dimensions not verified")
        else:
            command = [
                ffprobe, "-v", "error", "-select_streams", "v:0",
                "-show_entries", "stream=codec_name,width,height:format=duration,format_name",
                "-of", "json", str(path),
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode != 0:
                report["errors"].append(result.stderr.strip() or "ffprobe could not read the export")
            else:
                try:
                    data = json.loads(result.stdout)
                    streams = data.get("streams", [])
                    fmt = data.get("format", {})
                    if streams:
                        stream = streams[0]
                        report["video_stream_found"] = True
                        report["width"] = stream.get("width")
                        report["height"] = stream.get("height")
                    else:
                        report["errors"].append("No video stream found")
                    if fmt.get("duration") is not None:
                        report["duration_seconds"] = float(fmt["duration"])
                except (ValueError, TypeError, json.JSONDecodeError) as exc:
                    report["errors"].append(f"Invalid ffprobe metadata: {exc}")

    duration = report["duration_seconds"]
    if duration is not None:
        if duration < args.min_duration:
            report["errors"].append(f"Duration {duration:.3f}s is below minimum {args.min_duration:.3f}s")
        if args.max_duration is not None and duration > args.max_duration:
            report["errors"].append(f"Duration {duration:.3f}s exceeds maximum {args.max_duration:.3f}s")
    if args.expected_width is not None and report["width"] is not None:
        if report["width"] != args.expected_width:
            report["errors"].append(f"Expected width {args.expected_width}, got {report['width']}")
    if args.expected_height is not None and report["height"] is not None:
        if report["height"] != args.expected_height:
            report["errors"].append(f"Expected height {args.expected_height}, got {report['height']}")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"File: {report['file']}")
        print(f"Size: {report['size_bytes']} bytes")
        print(f"Duration: {report['duration_seconds'] if report['duration_seconds'] is not None else 'not verified'}")
        print(f"Dimensions: {report['width']}x{report['height']}" if report["width"] else "Dimensions: not verified")
        for note in report["notes"]:
            print(f"NOTE: {note}")
        for error in report["errors"]:
            print(f"ERROR: {error}")
        print("Playback itself is not verified by ffprobe; play the file to confirm.")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
