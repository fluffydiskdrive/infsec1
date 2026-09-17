#!/bin/bash

if [ $# -ne 2 ]; then
	echo "findocc <file> <key>"
	exit 1
fi

grep -o "$2" "$1" | wc -l

