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
      serialShell=$(finger | grep ttyAMA0)
      ssh=$(finger | grep pi | grep pts)
      if [ "$ssh" == "" ] && [ "$serialShell" == "" ]
      then
	echo 'nologon, shut down' >> $log
	date >> $log
  	#cat pwd.txt | sudo -S shutdown now
      fi
    fi
    takePhoto=$(python3 photoService.py)
  done

  sleep 15
done
