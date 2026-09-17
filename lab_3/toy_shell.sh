#!/bin/bash

while true; do
	read -p "toy_shell >" command
	if [ "$command" == "exit" ]; then
		exit 0
	fi
	if [ "$command" != "" ]; then
		if [[ "$command" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
			IFS=- read -r YEAR_I MONTH_I DAY_I <<< "$command"
			for file in ./*; do
				read -r DATE _ <<< "$(stat -c '%w' "$file")"
				IFS=- read -r YEAR MONTH DAY <<< "$DATE"
				if [ "$YEAR" -lt "$YEAR_I" ]; then
					continue
				fi
				if [ "$MONTH" -lt "$MONTH_I" ]; then
					continue
				fi
				if [ "$DAY" -ge "$DAY_I" ]; then
					continue
				fi
				echo "$file, created $DATE" 
			done
		else
			echo "Please use YYYY-MM-DD."
			continue
		fi
	fi
done
