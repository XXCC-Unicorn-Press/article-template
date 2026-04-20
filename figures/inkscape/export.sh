#!/usr/bin/env bash
set -euo pipefail

function export_svg_to_png() {
    local file="$1"
    local svg="${file%.*}.svg"
    local png="${file%.*}.png"
    if [[ ! -f "$png" || "$svg" -nt "$png" ]]; then
        echo "Exporting $svg to $png..."
        inkscape "$svg" --export-dpi=512 --export-type=png --export-filename="$png"
    else
        echo "Skipping $svg, PNG is up to date."
        return
    fi
}

if [ $# -eq 0 ]; then
    DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    find "$DIR" -maxdepth 1 -type f -name '*.svg' -print0 |
    while IFS= read -r -d '' svg; do
        export_svg_to_png "$svg"
    done
else
    for svg in "$@"; do
        export_svg_to_png "$svg"
    done
fi
