"""Draw the link preview image (static/og.png) and the favicon from the pixel sprites.

Run it again after changing the avatar or the name:

    python make_images.py
"""

from pathlib import Path

from PIL import Image, ImageDraw

from pixel_art import SPRITES

STATIC = Path(__file__).parent / "static"

BG = (11, 11, 12)
DOT = (30, 30, 32)
TEXT = (236, 236, 236)
ORANGE = (255, 130, 0)
SCREEN = (255, 138, 0)
INK = (28, 15, 0)
PLASTIC = (236, 235, 230)
BEZEL = (35, 35, 37)

# A tiny 5x7 pixel font with just the letters this image needs.
GLYPHS = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}


def draw_rows(draw: ImageDraw.ImageDraw, rows: list[str], x: int, y: int, scale: int, color) -> None:
    """Draw a pixel grid ("#" and "e" are filled) with its top left corner at x, y."""
    for row_index, row in enumerate(rows):
        for col_index, pixel in enumerate(row):
            if pixel in "#e":
                left, top = x + col_index * scale, y + row_index * scale
                draw.rectangle([left, top, left + scale - 1, top + scale - 1], fill=color)


def draw_text(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, scale: int, color) -> None:
    for i, letter in enumerate(text):
        draw_rows(draw, GLYPHS[letter], x + i * 6 * scale, y, scale, color)


def make_og_image() -> None:
    image = Image.new("RGB", (1200, 630), BG)
    draw = ImageDraw.Draw(image)

    for x in range(11, 1200, 22):
        for y in range(11, 630, 22):
            draw.point((x, y), fill=DOT)

    draw_text(draw, "TRISTAN", 72, 170, 12, TEXT)
    draw_text(draw, "HARTENSTEIN", 72, 284, 12, TEXT)
    draw.rectangle([72, 398, 216, 405], fill=ORANGE)
    draw_text(draw, "LEBENSLAUF", 72, 432, 6, ORANGE)

    # The device with the avatar on its screen
    draw.rounded_rectangle([900, 150, 1130, 480], radius=28, fill=PLASTIC)
    draw.ellipse([918, 166, 926, 174], fill=ORANGE)
    draw.rounded_rectangle([920, 190, 1110, 400], radius=12, fill=BEZEL)
    draw.rounded_rectangle([928, 198, 1102, 392], radius=6, fill=SCREEN)
    avatar = SPRITES["avatar"]
    scale = 9
    draw_rows(draw, avatar, 1015 - len(avatar[0]) * scale // 2, 218, scale, INK)
    draw.ellipse([985, 412, 1045, 472], fill=BEZEL)
    draw.ellipse([1003, 430, 1027, 454], fill=(58, 58, 61))

    image.save(STATIC / "og.png", optimize=True)


def make_favicon() -> None:
    size = 64
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=14, fill=SCREEN)
    head = SPRITES["avatar"][:14]
    scale = 3
    draw_rows(draw, head, (size - len(head[0]) * scale) // 2, 11, scale, INK)
    image.save(STATIC / "favicon.png")
    image.save(STATIC / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])


if __name__ == "__main__":
    make_og_image()
    make_favicon()
    print("Created static/og.png, static/favicon.png and static/favicon.ico")
