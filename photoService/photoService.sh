#!/bin/bash

while true
do

  log=/home/pi/rCamera/photoService/log.txt

  takePhoto=$(python3 photoService.py)
  while [[ "$takePhoto" == "true" || "$takePhoto" == "schedule" ]]
  do
    if [ "$takePhoto" == "schedule" ]
    then
      ./schedule.sh >> $log
      python3 featherCom.py >> $log
    elif [ "$takePhoto" == "true" ]
    then
      ./gpAutoTakePhoto.sh >> $log
      python3 featherCom.py >> $log
    fi
    takePhoto=$(python3 photoService.py)
  done

  sleep 15
done
