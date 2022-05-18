#!/bin/bash

echo "taking photo" >> log.txt
date >> log.txt

../focusCam.py

FILE=$(gphoto2 --capture-image-and-download --keep-raw | grep "Saving file as" | cut -c 16-50)
echo "Writing:" $FILE
mv $FILE ../../photos/
cd ../../photos
#convert $FILE -quality 75% -resize 15% $FILE-15.JPG;
#-quality 80%
#convert $FILE -quality 75% -resize 50% $FILE-50.JPG;

cd ../rCamera/MicroTimer

nextTime=$(head -1 timeQueue.txt)

echo $nextTime

python3 featherCom.py $nextTime 
sed -i 1d timeQueue.txt

