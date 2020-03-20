#!/bin/bash

SRC_FOLDERS=("01_generator" "02_splitter" "03_parser")

for SRC in "${SRC_FOLDERS[@]}"; do
    echo "--------------------------------------------"
    echo "I am in folder $SRC"
    echo "--------------------------------------------"

    cd $SRC
    for i in `find . -iname '*.m'`
    do
        cp $i ../;
    done
    cd ..
    make all mfiledir=docs/mfiles/$SRC
    rm *.m
done

mkdocs build
# mkdocs serve