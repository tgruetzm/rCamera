import sys
import time
import datetime
from datetime import datetime, timezone

tq = open('timeQueue.txt', 'r')
lines = tq.readlines()
tq.close()

nextLine = lines.pop(0).replace("\n","")
nextTime = datetime.strptime(nextLine, "%I:%M %p %Y-%m-%d")
print("photoService: next time:" + str(nextTime))

now = datetime.now()

if now > nextTime:
  tq = open("timeQueue.txt", "w") 
  tq.writelines(lines)
  tq.close() 
  return "true"
return "false"

