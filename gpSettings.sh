#!/bin/bash
./focusCam.py


#aperture
if [ "$1" == "ap" ] && [ "$#" -eq 1 ]
then
	gphoto2 --get-config /main/capturesettings/aperture
elif [ "$1" == "ap" ] && [ "$#" -eq 2 ]
then
	gphoto2 --set-config /main/capturesettings/aperture=$2
	gphoto2 --get-config /main/capturesettings/aperture
#shutterspeed
elif [ "$1" == "ss" ] && [ "$#" -eq 1 ]
then
	gphoto2 --get-config /main/capturesettings/shutterspeed
	
elif [ "$1" == "ss" ] && [ "$#" -eq 2 ]
then
	gphoto2 --set-config /main/capturesettings/shutterspeed=$2
	gphoto2 --get-config /main/capturesettings/shutterspeed
#iso
elif [ "$1" == "iso" ] && [ "$#" -eq 1 ]
then
	gphoto2 --get-config /main/imgsettings/iso
elif [ "$1" == "iso" ] && [ "$#" -eq 2 ]
then
	gphoto2 --set-config /main/imgsettings/iso=$2
	gphoto2 --get-config /main/imgsettings/iso
#exposurecompensation
elif [ "$1" == "ec" ] && [ "$#" -eq 1 ]
then
	gphoto2 --get-config /main/capturesettings/exposurecompensation
elif [ "$1" == "ec" ] && [ "$#" -eq 2 ]
then
	gphoto2 --set-config /main/capturesettings/exposurecompensation=$2
	gphoto2 --get-config /main/capturesettings/exposurecompensation

#autoexposuremodedial
elif [ "$1" == "aem" ] && [ "$#" -eq 1 ]
then
	gphoto2 --get-config /main/capturesettings/autoexposuremodedial
elif [ "$1" == "aem" ] && [ "$#" -eq 2 ]
then
	gphoto2 --set-config /main/capturesettings/autoexposuremode=$2
	gphoto2 --get-config /main/capturesettings/autoexposuremode
		
else

	value=$(gphoto2 --get-config /main/capturesettings/aperture | grep Current | cut -c 9-50)
	echo "Aperature: " $value

	value=$(gphoto2 --get-config /main/capturesettings/shutterspeed | grep Current | cut -c 9-50)
	echo "Shutter Speed: " $value

	value=$(gphoto2 --get-config /main/imgsettings/iso | grep Current | cut -c 9-50)
	echo "ISO: " $value

	value=$(gphoto2 --get-config /main/capturesettings/exposurecompensation | grep Current | cut -c 9-50)
	echo "Exposure Comp: " $value
	
	value=$(gphoto2 --get-config /main/capturesettings/autoexposuremode | grep Current | cut -c 9-50)
	echo "Exposure Mode: " $value
	
fi

