#!/usr/bin/env python3
"""
Regenerate the Murmur icon set (three black dots on white background)
at all required sizes. Run from the repo root:

    python3 icons/make-icons.py

Requires Pillow:  pip3 install --user Pillow
"""
import os
from PIL import Image, ImageDraw

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
INK = (14, 14, 16, 255)        # --ink, matches the app
BG  = (255, 255, 255)          # solid white per Apple's recommendation

SIZES = {
    "apple-touch-icon.png": 180,   # iOS home screen
    "icon-192.png":         192,   # Android
    "icon-512.png":         512,   # PWA hi-res
    "favicon-32.png":        32,   # browser tab
    "favicon-16.png":        16,
}

def make(size, path):
    img = Image.new("RGB", (size, size), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    diameter = int(size * 0.18)
    gap = int(size * 0.10)
    span = diameter * 3 + gap * 2
    left = (size - span) // 2
    cy = size // 2
    for i in range(3):
        cx = left + diameter // 2 + i * (diameter + gap)
        draw.ellipse(
            (cx - diameter // 2, cy - diameter // 2,
             cx + diameter // 2, cy + diameter // 2),
            fill=INK,
        )
    img.save(path, "PNG", optimize=True)
    print(f"  {os.path.basename(path):<24} {size}×{size}")

if __name__ == "__main__":
    print("generating murmur icons:")
    for name, size in SIZES.items():
        make(size, os.path.join(OUT_DIR, name))
    print("done.")
