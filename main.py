#!/usr/bin/env python3
"""
main.py - Entry script for the make.fun bounty "news-image-20261119".

This script locates the pre-rendered newspaper front page entry image ('entry.png')
relative to its own directory, determines the target output directory from the
MAKEFUN_OUTPUT_DIR environment variable (falling back to '/output'), ensures
the directory exists, and copies the image bytes to '<output>/entry.png'.
"""

import os
import sys
from pathlib import Path


def main() -> None:
    # Resolve the script's own directory to locate entry.png reliably
    script_dir = Path(__file__).resolve().parent
    source_image = script_dir / "entry.png"

    # Get output directory from environment variable or default to /output
    output_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_str)

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    target_image = output_dir / "entry.png"

    # Read bytes from source and write to target
    image_bytes = source_image.read_bytes()
    target_image.write_bytes(image_bytes)

    # Read-back verification
    if not target_image.exists():
        print(f"Error: Target image {target_image} is missing after write.", file=sys.stderr)
        sys.exit(1)

    written_bytes = target_image.read_bytes()
    if len(written_bytes) != len(image_bytes):
        print(
            f"Error: Byte length mismatch. Source: {len(image_bytes)}, written: {len(written_bytes)}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
