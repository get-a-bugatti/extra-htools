#!/bin/bash

# Check if two files are provided as arguments
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file1> <file2>"
  exit 1
fi

# Assign the files to variables
file1="$1"
file2="$2"

# Determine which file is bigger
if [ $(wc -l < "$file1") -ge $(wc -l < "$file2") ]; then
  larger_file="$file1"
  smaller_file="$file2"
else
  larger_file="$file2"
  smaller_file="$file1"
fi

# Compare lines and output lines from the smaller file not in the larger file to not-in.txt
grep -Fxv -f "$larger_file" "$smaller_file" > not-in.txt

echo "Lines from the smaller file that are not in the larger file have been saved to 'not-in.txt'."

