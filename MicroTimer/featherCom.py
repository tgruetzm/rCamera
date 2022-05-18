import serial
import sys
import datetime
from datetime import datetime, timezone

# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# arg3 = sys.argv[3]

# nextTime = datetime.strptime(arg1 + " " + arg2 + " " + arg3, "%I:%M %p %Y-%m-%d")

# nextTimeString = str(nextTime.timestamp()) + "\n"
# print(nextTimeString)


ser = serial.Serial('/dev/ttyAMA1')  # open serial port

now = datetime.now(timezone.utc)

output = "hello feather," + now.isoformat() + "\n"

print("pi:" + output)

ser.write(bytes(output,"ascii"))     # write a string
ser.flush()

message = []
while True:
  data = ser.read(1)
  if data is not None:
    if chr(data[0]) == "\n":
      break
    message.append(chr(data[0]))

message_string = "".join(message)

if message_string == 'send next time':
    print("f:" + message_string)

tq = open('timeQueue.txt', 'r')
lines = tq.readlines()

message = []
while True:
  data = ser.read(1)
  if data is not None:
    if chr(data[0]) == "\n":
      break
    message.append(chr(data[0]))

message_string = "".join(message)

nextTimeString = str(nextTime.timestamp()) + "\n"
print(nextTimeString)

print("pi:" + nextTimeString)
ser.write(bytes(nextTimeString,"ascii"))
ser.flush()

ser.close()             # close port
