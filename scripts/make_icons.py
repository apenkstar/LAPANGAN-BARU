"""Membuat ikon aplikasi (lapangan putih di atas hijau) untuk @capacitor/assets."""
import os
from PIL import Image, ImageDraw

S = 1024
GREEN = (14, 124, 82, 255)
WHITE = (255, 255, 255, 255)
os.makedirs("assets", exist_ok=True)

def court(draw):
    w = 26
    x0, y0, x1, y1 = 322, 232, 702, 792
    draw.rounded_rectangle((x0, y0, x1, y1), radius=18, outline=WHITE, width=w)
    cy = (y0 + y1) // 2
    draw.line((x0, cy, x1, cy), fill=WHITE, width=w)
    cx = (x0 + x1) // 2
    r = 92
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=WHITE, width=w)
    # kotak area di kedua ujung
    bw, bh = 170, 120
    draw.rectangle((cx - bw // 2, y0, cx + bw // 2, y0 + bh), outline=WHITE, width=w)
    draw.rectangle((cx - bw // 2, y1 - bh, cx + bw // 2, y1), outline=WHITE, width=w)

bg = Image.new("RGBA", (S, S), GREEN)
bg.save("assets/icon-background.png")

fg = Image.new("RGBA", (S, S), (0, 0, 0, 0))
court(ImageDraw.Draw(fg))
fg.save("assets/icon-foreground.png")

full = Image.new("RGBA", (S, S), GREEN)
court(ImageDraw.Draw(full))
full.save("assets/icon-only.png")
print("ikon dibuat")
