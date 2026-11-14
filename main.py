"""Entry for make.fun food-picture-01: write the food picture to /output/entry.png.

The entry image is a JPEG file (food.jpg) held in this repository. The
competition allows the output file to be a PNG or a JPEG, told apart by
its first bytes, while the name stays entry.png. This program copies the
image byte-for-byte, so two runs always write identical bytes. It uses
only the Python standard library, needs no network, and writes only to
the output directory (MAKEFUN_OUTPUT_DIR when set, otherwise /output).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "food.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Self-check: the written file must be byte-identical to the source.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise SystemExit("output size mismatch: wrote %d bytes, expected %d"
                         % (os.path.getsize(DST), os.path.getsize(SRC)))
    print("Wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
