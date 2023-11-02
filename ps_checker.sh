#!/bin/bash

process=$(ps -A | grep python3)
logfile="$(pwd)/alertskh.log"
main="$(pwd)/main.py"

if [[ -z $process ]]; then
        echo -e "$(date +"%Y-%m-%d %T.%N") Process not found. Starting..." >> $logfile
        python3 $main &
fi