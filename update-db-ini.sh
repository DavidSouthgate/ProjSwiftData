#!/bin/sh
wget https://download.osgeo.org/proj/proj-9.2.0.tar.gz -O proj.tar.gz
mkdir tmp
tar -xvf "proj.tar.gz" -C "tmp" --strip-components=1
mkdir tmp/build
cd tmp/build
cmake ..
make generate_proj_db
mv data/proj.db ../..
mv data/proj.ini ../..
cd ../..
rm -rf tmp
rm -rf proj.tar.gz