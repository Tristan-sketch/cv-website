"""Pixel art drawn in plain Python and rendered as SVG.

Each sprite is a list of rows: "#" is a filled pixel, "e" is an eye pixel
(it blinks via CSS) and "." is empty.
"""

from markupsafe import Markup

SPRITES = {
    "avatar": [
        ".....######.....",
        "...##########...",
        "..############..",
        "..##.##.##.###..",
        "..#..........#..",
        "..#..........#..",
        "..#..ee..ee..#..",
        "..#..ee..ee..#..",
        "..#..........#..",
        "..#..........#..",
        "..#..#....#..#..",
        "..#...####...#..",
        "...#........#...",
        "....########....",
        "......#..#......",
        "..############..",
        ".##############.",
    ],
    "user": [
        "...###...",
        "..#####..",
        "..#####..",
        "...###...",
        ".........",
        "..#####..",
        ".#######.",
        ".#######.",
        ".#######.",
    ],
    "terminal": [
        "#########",
        "#.......#",
        "#.#.....#",
        "#..#....#",
        "#.#..##.#",
        "#.......#",
        "#########",
    ],
    "briefcase": [
        "...###...",
        "...#.#...",
        "#########",
        "#.......#",
        "####.####",
        "#.......#",
        "#########",
    ],
    "star": [
        "....#....",
        "...###...",
        "#########",
        ".#######.",
        "..#####..",
        "..##.##..",
        ".##...##.",
    ],
    "cap": [
        "....#....",
        "..#####..",
        "#########",
        "..#####.#",
        "..#####.#",
        "...###..#",
    ],
    "heart": [
        ".##...##.",
        "####.####",
        "#########",
        ".#######.",
        "..#####..",
        "...###...",
        "....#....",
    ],
    "check": [
        "........#",
        ".......##",
        "#.....##.",
        "##...##..",
        ".##.##...",
        "..###....",
        "...#.....",
    ],
    "printer": [
        "..#####..",
        "..#...#..",
        "#########",
        "#.......#",
        "#.....#.#",
        "#########",
        "..#...#..",
        "..#####..",
    ],
    "mail": [
        "#########",
        "##.....##",
        "#.#...#.#",
        "#..#.#..#",
        "#...#...#",
        "#.......#",
        "#########",
    ],
}

# Catch typos in the drawings early: every row of a sprite must be equally wide.
for _name, _rows in SPRITES.items():
    assert len({len(row) for row in _rows}) == 1, f"Sprite '{_name}' has rows of different width"


def pixel_svg(name: str, scale: int = 4, css_class: str = "") -> Markup:
    """Render a sprite as an inline SVG. The pixels use the current text color."""
    rows = SPRITES[name]
    width, height = len(rows[0]), len(rows)
    rects = []
    for y, row in enumerate(rows):
        for x, pixel in enumerate(row):
            if pixel == "#":
                rects.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')
            elif pixel == "e":
                rects.append(f'<rect class="eye" x="{x}" y="{y}" width="1" height="1"/>')
    return Markup(
        f'<svg class="pixel {css_class}" viewBox="0 0 {width} {height}" '
        f'width="{width * scale}" height="{height * scale}" fill="currentColor" '
        f'shape-rendering="crispEdges" aria-hidden="true">{"".join(rects)}</svg>'
    )
