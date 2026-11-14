# Food picture entry — make.fun food-picture-01

An entry for the make.fun food-picture bounty: one picture of food,
produced by a small Python program that copies the bundled photo to
the output path the grader reads.

## The photo

`food.jpg` is a close-up photograph of a gourmet cheeseburger: a glossy
toasted brioche bun, cheddar melting down the sides, a grilled beef
patty, lettuce and tomato, warm golden light and a little steam, all
against a dark background so the dish stays readable at small sizes.
The file is a JPEG, 1024 by 1024 pixels, 257,009 bytes — inside the
one-mebibyte limit.

## The program

`main.py` runs on Python 3.13 with the standard library only. It checks
that `food.jpg` starts with the JPEG magic bytes, copies it unchanged
to `entry.png` inside the output directory (`MAKEFUN_OUTPUT_DIR` when
set, `/output` otherwise), then confirms the copy has the same size and
the same leading bytes. No network, no randomness, no clock: running it
twice writes identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/check-out python3 main.py
```

## Files in this repository

- `main.py` — the program that writes the entry
- `food.jpg` — the cheeseburger photograph
- `LICENSE` — MIT licence text
- `README.md` — this note
