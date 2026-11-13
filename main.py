"""Write the AI coding agent joke to the make.fun output file.

Run locally with: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
Use --check to validate the joke without writing an output file.
"""

import argparse
import os
from pathlib import Path

JOKE = "My AI coding agent called the refactor behavior-preserving; it had preserved the bug’s behavior."


def validate_joke() -> None:
    if not JOKE.strip():
        raise SystemExit("Error: joke must not be blank")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit("Error: joke must be between 1 and 280 Unicode code points")


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the make.fun joke entry")
    parser.add_argument("--check", action="store_true", help="validate the joke without writing it")
    args = parser.parse_args()

    validate_joke()
    if args.check:
        return

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
