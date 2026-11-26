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
    try:
        destination.mkdir(parents=True, exist_ok=True)
    except (FileExistsError, NotADirectoryError):
        parser.error(f"output destination is not a directory: {destination}")
    except OSError as error:
        parser.error(f"cannot create output directory {destination}: {error.strerror}")
    copyfile(Path(__file__).resolve().with_name("entry.png"), destination / "entry.png")


if __name__ == "__main__":
    main()
