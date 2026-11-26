"""Write the bundled editorial image to the grader output directory."""
import argparse
import os
from pathlib import Path
from shutil import copyfile


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"),
        help="destination directory (default: MAKEFUN_OUTPUT_DIR or /output)",
    )
    destination = parser.parse_args().output_dir
    destination.mkdir(parents=True, exist_ok=True)
    copyfile(Path(__file__).resolve().with_name("entry.png"), destination / "entry.png")


if __name__ == "__main__":
    main()
