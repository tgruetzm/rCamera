#!/bin/bash

log=/home/pi/rCamera/inactivityService/log.txt

../focusCam.py

#gettime
date=$(gphoto2 --get-config /main/settings/datetimeutc | grep Current: | cut -c 10-40)
echo "setting time to: " >> $log
cat pwd.txt | sudo -S date -s "@$date" >> $log

while true
do
  sleep 240
  duration=$(finger | grep ttyAMA0 | cut -c 41-45)
  ssh=$(finger | grep pi | grep pts)
  
  echo "duration:" $duration >> $log

  if [ "$ssh" != "" ]
  then
	echo 'ssh in progress dont shutdown' >> $log
        date >> $log
	continue
  fi
  if [ "$duration" == "" ]  
  then 
	echo 'nologon' >> $log
	date >> $log
  	cat pwd.txt | sudo -S shutdown now
  elif (( $duration > 1 ))
  then 
	echo 'inactive' >> $log
        date >> $log
	cat pwd.txt | sudo -S shutdown now
  fi
done
