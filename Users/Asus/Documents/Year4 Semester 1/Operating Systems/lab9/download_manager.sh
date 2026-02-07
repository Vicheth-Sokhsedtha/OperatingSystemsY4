#!/bin/bash

# Download Manager Script

# Loop through all files in current directory
for file in *; do
    # Skip directories
    [ -f "$file" ] || continue
    
    # Extract file extension
    EXT="${file##*.}"
    EXT_LOWER=$(echo "$EXT" | tr '[:upper:]' '[:lower:]')

    # If file has no extension, skip
    if [ "$file" = "$EXT" ]; then
        EXT_LOWER="others"
    fi

    # Create folder if not exists
    mkdir -p "$EXT_LOWER"

    # Move file to folder
    mv "$file" "$EXT_LOWER/"
done

echo "Files organized by extension."