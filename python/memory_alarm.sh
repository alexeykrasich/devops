#!/bin/bash
###----------------------------------------------------
#-Owner: Alexey Krasichonak
#-Discription: Send an alarm to API if memory usage greater than 80%
#----------------------


##>>>>>>>>>>>VARIABLES<<##
MEMORY_PRC=$(free -m | awk 'NR==2{printf "%.0f", $3*100/$2 }')


##>>>>>>>>>>>BODY<<##
if [[ $MEMORY_PRC -gt '80' ]]; then echo "ALARM! Memory usage is more than 80% $" >> alarm.log;  fi
