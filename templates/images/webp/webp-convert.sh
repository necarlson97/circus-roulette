#!/bin/bash

PARAMS=('')

if [ $# -ne 0 ]; then
    PARAMS=$@;
fi

cd $(pwd)

shopt -s nullglob nocaseglob extglob

for FILE in *.@(webp); do
    dwebp $PARAMS "$FILE" -o "${FILE%.*}".png;
done
