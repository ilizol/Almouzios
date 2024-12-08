#!/usr/bin/env python3

import fontforge
from pathlib import Path

font = fontforge.open("../../Almouzios.otf")
# font = fontforge.open("../../sources/Almouzios.sfd")


for glyph in (char for char in font.glyphs() if 57344 <= char.unicode <= 63743):
    name = glyph.glyphname
    unicode = f"0x{hex(glyph.unicode).replace('0x', '').upper()}"
    widthlist_item = f"{unicode} {name}"
    width = glyph.width
    leftSB = round(glyph.left_side_bearing, 2)
    rightSB = round(glyph.right_side_bearing, 2)
    widthlist_item += f"\n\twidth: {width}"
    widthlist_item += f"\n\tleftSB: {leftSB}"
    widthlist_item += f"\n\trightSB: {rightSB}"

    print(widthlist_item)
