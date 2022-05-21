#!/bin/bash
 
while true
do
  sleep 15
  
  takePhoto = "true"

  while [ takePhoto == "true" ]
  do
    takePhoto=$(python3 photoService.py >> log.txt)
    if [ takePhoto == "true" ]
      ./gpAutoTakePhoto.sh >> log.txt
    fi
  done
  

  # shutdown if no one is logged int
  duration=$(finger | grep ttyAMA0 | cut -c 41-45)
  ssh=$(finger | grep pi | grep pts)
  
  echo "duration:" $duration >> /home/pi/rCamera/inactivityService/out.log

  if [ "$ssh" != "" ]
  then
	echo 'ssh in progress dont shutdown' >> /home/pi/rCamera/inactivityService/out.log
        date >> /home/pi/rCamera/inactivityService/out.log
	continue
  fi  
  if [ "$duration" == "" ]  
  then 
	echo 'nologon' >> /home/pi/rCamera/inactivityService/out.log	
	date >> /home/pi/rCamera/inactivityService/out.log
  	cat pwd.txt | sudo -S shutdown now
  fi
done
