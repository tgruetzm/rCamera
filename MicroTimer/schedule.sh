#!/bin/bash

while IFS= read -r line; do
  echo "scheduling for %s\n'" "$line" >> log.txt
  at -f gpAutoTakePhoto.sh "$line"
  echo $line >> timeQueue.txt
done < <(python3 Times.py)

python3 featherCom.py >> log.txt

