#!/bin/bash

END_TIME_H=18
END_TIME_M=0

CURR_TIME_H=$(date +"%H")
CURR_TIME_M=$(date +"%M")

TIME_DIFF_TOTAL=$(((END_TIME_H * 60 + END_TIME_M) - (CURR_TIME_H * 60 + CURR_TIME_M)))
TIME_DIFF_M=$((TIME_DIFF_TOTAL % 60))
TIME_DIFF_H=$(((TIME_DIFF_TOTAL - TIME_DIFF_M) / 60))

date +"Current time: %H:%M"
echo "Work day ends after $TIME_DIFF_H hours and $TIME_DIFF_M minutes."
