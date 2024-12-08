python3 generate-font.py ../../sources/Almouzios.sfd ../../Almouzios.otf
python3 generate-font-metadata.py ../../sources/Almouzios.sfd ../metadata/glyphnames.json

mv *.metadata.json ../..

#######################################################
# DEBUG
./generate-anchorlist.py > ../../sources/anchorlist.txt
./generate-glyph-table.py > html/glyphs.html
./generate-images.py
./generate-metricslist.py > ../../sources/metricslist.txt
./generate-namelist.py > ../../sources/namelist.txt
#######################################################

cp -f ../../Almouzios.metadata.json ../../../neanes/src/assets/fonts/Almouzios.metadata.json
cp -f ../../Almouzios.otf ../../../neanes/src/assets/fonts/Almouzios.otf
