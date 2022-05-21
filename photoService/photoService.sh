#!/bin/bash
 
while true
do

  takePhoto="true"

  while [ "$takePhoto" == "true" ]
  do
    takePhoto=$(python3 photoService.py)
    echo $takePhoto
    if [ "$takePhoto" == "true" ]
    then
      ./gpAutoTakePhoto.sh
      python3 featherCom.py
    fi
  done

  sleep 15
  # shutdown if no one is logged int
  duration=$(finger | grep ttyAMA0 | cut -c 41-45)
  ssh=$(finger | grep pi | grep pts)

  if [ "$ssh" != "" ]
  then
	continue
  fi
  if [ "$duration" == "" ]  
  then
	echo 'nologon' 
	date
  	cat pwd.txt | sudo -S shutdown now
  fi

done
