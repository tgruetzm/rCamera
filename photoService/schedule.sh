#!/bin/bash

while IFS= read -r line; do
  echo "scheduling for %s\n'" "$line"
  echo $line >> timeQueue.txt
done < <(python3 TimeScheduler.py)

python3 featherCom.py

