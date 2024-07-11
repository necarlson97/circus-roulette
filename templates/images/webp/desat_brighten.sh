for file in *.{jpg,jpeg,png,bmp,tiff,gif,webp}; do convert "$file" -colorspace Gray -level 0x90% "${file%.*}_bw.png"; done
