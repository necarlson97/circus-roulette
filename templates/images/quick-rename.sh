#!/bin/bash

# Loop through all PNG files in the directory
for file in *.png; do
    # Extract the base name without the extension
    base_name="${file%.png}"

    # Rename the file by adding '-1' before the '.png' extension
    mv "$file" "${base_name}-1.png"
done

echo "Renaming complete."
