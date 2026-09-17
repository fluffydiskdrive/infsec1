#!/bin/bash

if [ $# -ne 1 ]; then
	echo "delete_empty_files <dir>"
	exit 1
fi
if [ ! -d "$1" ]; then
	echo "err: arg is not a dir"
	exit 1
fi
for file in "$1"/*; do
	if [ ! -s "$file" ]; then
		echo "Deleted: $file"
		rm "$file"
	fi
done
