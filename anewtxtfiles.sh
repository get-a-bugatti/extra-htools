#!/bin/bash

# Create or clear the new results file
> results.txt

# Loop through all .txt files in the current directory
for file in *.txt; do
    # Skip the results file itself if it exists in the same directory
    if [ "$file" != "results.txt" ]; then
        # Use anew to add unique lines to results.txt
        cat "$file" | anew results.txt
    fi
done

echo "Unique lines from .txt files added to results.txt"

