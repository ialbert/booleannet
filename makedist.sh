python.bat setup.py install
python.bat setup.py bdist_wininst
python.bat setup.py sdist
cp dist/*.exe docs/windows
cp dist/*.zip docs/windows
cd docs
zip windows-quickstart.zip  -u -r windows/*
scp booleannet.html webserver@atlas.bx.psu.edu:/export/home/webserver/www/atlas.bx.psu.edu/htdocs/booleannet
scp png/* webserver@atlas.bx.psu.edu:/export/home/webserver/www/atlas.bx.psu.edu/htdocs/booleannet/png
scp windows-quickstart.zip webserver@atlas.bx.psu.edu:/export/home/webserver/www/atlas.bx.psu.edu/htdocs/booleannet
