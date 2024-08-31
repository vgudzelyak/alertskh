#!/bin/bash

process=$(ps aux | grep '[a]lertskh/main.py')
logfile="$(pwd)/alertskh.log"
main="$(pwd)/main.py"

if [[ -z $process ]]; then
        echo -e "$(date +"%Y-%m-%d %T.%N") Process not found. Starting..." >> $logfile
        python3 $main &
fi