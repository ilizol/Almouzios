#!/usr/bin/env python3

import fontforge
from pathlib import Path

# font = fontforge.open("../../Almouzios.otf")
font = fontforge.open("../../sources/Almouzios.sfd")


for glyph in (char for char in font.glyphs() if 57344 <= char.unicode <= 63743):
    name = glyph.glyphname
    anchorPoints = glyph.anchorPoints
    unicode = f"0x{hex(glyph.unicode).replace('0x', '').upper()}"
    anchorlist_item = f"{unicode} {name}"
    for i, anchor in enumerate(anchorPoints):
        anchor_name = anchor[0]
        anchorlist_item += f"\n\t{anchor}"

    print(anchorlist_item)
