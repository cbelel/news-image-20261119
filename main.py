#!/usr/bin/env python3
"""
main.py - Copies entry.png to the target make.fun output directory with byte verification.
Part of the classic-newspaper revision of the news-image-20261119 entry, summarizing
Thursday 19 November 2026 world news in a dense, information-rich 1024x1024 front page.
"""

import os
import sys

def main():
    # Resolve script directory and source image path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")
    
    # Determine output directory from environment variable or default to /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    dest_path = os.path.join(output_dir, "entry.png")
    
    if not os.path.exists(src_path):
        print(f"Error: Source image 'entry.png' not found at expected path: {src_path}", file=sys.stderr)
        sys.exit(1)
        
    # Read source bytes
    with open(src_path, "rb") as f:
        src_bytes = f.read()
        
    # Write destination bytes
    with open(dest_path, "wb") as f:
        f.write(src_bytes)
        
    # Verify destination exists and byte length matches
    if not os.path.exists(dest_path):
        print(f"Error: Destination file missing at {dest_path}", file=sys.stderr)
        sys.exit(1)
        
    with open(dest_path, "rb") as f:
        dest_bytes = f.read()
        
    if len(src_bytes) != len(dest_bytes):
        print(f"Error: Byte length mismatch! Source ({len(src_bytes)}) != Dest ({len(dest_bytes)})", file=sys.stderr)
        sys.exit(1)
        
    print(f"Successfully copied entry.png ({len(src_bytes)} bytes) to {dest_path}")

if __name__ == "__main__":
    main()
