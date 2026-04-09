#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

find "$DIR" -maxdepth 1 -type f -name '*.svg' -print0 |
while IFS= read -r -d '' svg; do
    png="${svg%.svg}.png"
    inkscape "$svg" --export-dpi=512 --export-type=png --export-filename="$png"
done
