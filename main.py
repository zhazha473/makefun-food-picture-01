"""food-picture-01: copy the bundled food photo to the entry output.

The picture lives in this repository as food.jpg. The contest takes the
output file under the fixed name entry.png and tells a JPEG from a PNG
by its first bytes, so copying the JPEG unchanged is a valid entry.
The script needs nothing but the standard library, touches no network,
and never uses the clock or randomness, so every run writes the same
bytes to the same place.
"""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(BASE_DIR, "food.jpg")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUTPUT_DIR, "entry.png")
JPEG_MAGIC = b"\xff\xd8\xff"


def build_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(SOURCE, "rb") as handle:
        head = handle.read(len(JPEG_MAGIC))
    if head != JPEG_MAGIC:
        raise SystemExit("food.jpg is not a JPEG file")
    shutil.copyfile(SOURCE, TARGET)
    written = os.path.getsize(TARGET)
    expected = os.path.getsize(SOURCE)
    if written != expected:
        raise SystemExit(
            "entry.png is %d bytes, expected %d" % (written, expected)
        )
    with open(TARGET, "rb") as handle:
        out_head = handle.read(len(JPEG_MAGIC))
    if out_head != JPEG_MAGIC:
        raise SystemExit("entry.png does not start with JPEG magic")
    print("entry.png ready: %d bytes at %s" % (written, TARGET))


if __name__ == "__main__":
    build_entry()
