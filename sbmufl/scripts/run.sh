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

# neanes
cp -f ../../almouzios.metadata.json ../../../neanes/src/assets/fonts/almouzios.metadata.json
cp -f ../../Almouzios.otf ../../../neanes/src/assets/fonts/Almouzios.otf

# neanestex
cp -f ../../almouzios.metadata.json ../../../neanestex/examples/almouzios.metadata.json
cp -f ../../Almouzios.otf ../../../neanestex/examples/Almouzios.otf

# poc-neanes-pdfgen
cp -f ../../almouzios.metadata.json ../../../poc-neanes-pdfgen/src/support/neanes/assets/almouzios.metadata.json
cp -f ../../Almouzios.otf ../../../poc-neanes-pdfgen/src/support/neanes/assets/Almouzios.otf
