#!/usr/bin/env python3

import fontforge
from pathlib import Path

font = fontforge.open("../../NeanesAlmouzios.otf")


for glyph in (char for char in font.glyphs() if 57344 <= char.unicode <= 63743):
    name = glyph.glyphname
    unicode = f"0x{hex(glyph.unicode).replace('0x', '').upper()}"
    namelist_item = f"{unicode} {name}"

    print(namelist_item)
