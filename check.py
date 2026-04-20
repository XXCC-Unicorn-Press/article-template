import os
import sys
from pathlib import Path


def check_pdf_status(main_name):
    # Locate the script directory and change to it
    script_dir = Path(__file__).parent.resolve()
    os.chdir(script_dir)

    pdf_file = script_dir / f"{main_name}.pdf"

    # Check if the PDF file exists
    if not pdf_file.exists():
        print("PDF is not found. Please build the PDF first.", file=sys.stderr)
        sys.exit(1)

    pdf_mtime = pdf_file.stat().st_mtime

    # Define the set of source file extensions to check
    source_extensions = {
        ".tex",
        ".bib",
        ".cls",
        ".sty",
        ".svg",
        ".png",
        ".jpg",
        ".jpeg",
        ".pdf",
    }

    latest_mtime = 0
    latest_file = ""

    # Find all source files recursively and check their modification times
    for path in script_dir.rglob("*"):
        # Exclude the PDF file itself
        if path.suffix.lower() in source_extensions and path != pdf_file:
            mtime = path.stat().st_mtime
            if mtime > latest_mtime:
                latest_mtime = mtime
                latest_file = path.name

    # Compare the latest modification time of source files with the PDF's
    if latest_mtime > pdf_mtime:
        print(f"PDF is outdated. Latest source file: {latest_file}", file=sys.stderr)
        sys.exit(1)
    else:
        print("PDF is up to date.")
        sys.exit(0)


if __name__ == "__main__":
    check_pdf_status("main")
