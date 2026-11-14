# make.fun — food-picture-01 entry

Entry for the make.fun bounty **"Make the best-looking food picture"**
($250, 100 paid places). The program writes one picture of food to
`/output/entry.png`.

## The picture

A photorealistic close-up of a gourmet cheeseburger: glossy toasted
brioche bun, melted cheddar dripping down the sides, juicy grilled beef
patty, fresh lettuce and tomato, warm golden light, steam rising — shot
against a simple dark background so the dish reads clearly even small.

- File: `food.jpg` (JPEG, 1024x1024, 257,009 bytes — under the 1 MiB limit)
- The output file is named `entry.png` as required; the competition
  accepts a PNG or a JPEG, told apart by its first bytes.

## How it works

`main.py` (Python 3.13, standard library only) copies `food.jpg`
byte-for-byte to `entry.png` in the output directory. No network, no
randomness, no timestamps — two runs write identical bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `food.jpg` — the food picture
- `LICENSE` — MIT
- `README.md` — this file

## Verification

Ran `main.py` three times (two runs with `MAKEFUN_OUTPUT_DIR` set to
different directories, one run with the default `/output` path). All
three outputs are byte-identical to each other and to `food.jpg`
(matching SHA-256). Output: JPEG, 1024x1024, 257,009 bytes.
