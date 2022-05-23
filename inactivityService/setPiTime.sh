#!/bin/bash
./focusCam.py


#gettime
date=$(gphoto2 --get-config /main/settings/datetimeutc | grep Current: | cut -c 10-40)
echo "setting time to: "
sudo date -s '@$date'

