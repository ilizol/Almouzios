python3 generate-font.py ../../sources/Almouzios.sfd ../../Almouzios.otf
python3 generate-font-metadata.py ../../sources/Almouzios.sfd ../metadata/glyphnames.json

mv *.metadata.json ../..

#######################################################
# DEBUG
./generate-anchorlist.py > ../../sources/anchorlist.txt
./generate-glyph-table.py > html/glyphs.html
./generate-images.py
./generate-namelist.py > ../../sources/namelist.txt
#######################################################