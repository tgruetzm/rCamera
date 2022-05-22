#!/bin/bash
 
while true
do
  sleep 90
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
  elif (( $duration > 1 ))
  then 
	echo 'inactive' >> /home/pi/rCamera/inactivityService/out.log
        date >> /home/pi/rCamera/inactivityService/out.log
	cat pwd.txt | sudo -S shutdown now
  fi
done
