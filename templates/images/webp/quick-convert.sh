for file in *.webp; do convert "$file" "${file%.webp}.png"; done
