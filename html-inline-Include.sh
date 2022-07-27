#!/usr/bin/bash
# set -x
# set -v
mkdir -p build
find -maxdepth 1 -iname "*.html"  -exec bash -c './build.py {} > ./build/{}' \;