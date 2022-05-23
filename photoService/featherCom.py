#!/usr/bin/env python
import serial
import sys
import time
import datetime
from datetime import datetime, timezone
import RPi.GPIO as GPIO

waitMax = 9; # seconds

def resetFeather():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)

    GPIO.output(23, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(5)

def handshake():
    now = datetime.now(timezone.utc)
    output = "hello feather," + now.isoformat() + "\n"
    print("pi:" + output)

    ser.write(bytes(output,"ascii"))     # write a string
    ser.flush()

    message = []
    while True:
        now = time.time()
        if now >= startTime + waitMax:
            return False
        data = ser.read(1)
        # print(data)
        if data != b'':
            if chr(data[0]) == "\n":
               break
            message.append(chr(data[0]))

        message_string = "".join(message)

    if message_string == 'ack':
        print("f:" + message_string)
        return True

def negotiateNextTime():
    message = []
    while True:
        now = time.time()
        if now >= startTime + waitMax:
            return False
        data = ser.read(1)
        # print(data)
        if data != b'':
            if chr(data[0]) == "\n":
               break
            message.append(chr(data[0]))

    message_string = "".join(message)

    if message_string == 'send next time':
        print("f:" + message_string)

    tq = open('timeQueue.txt', 'r')
    lines = tq.readlines()
    tq.close()


    while message_string == "send next time":
        message = []
        if len(lines) == 0:
            break

        nextLine = lines.pop(0).replace("\n","")
        nextTime = datetime.strptime(nextLine, "%I:%M %p %Y-%m-%d")
        print("pi: next time:" + str(nextTime))
        nextTimeString = str(nextTime.timestamp()) + "\n"

        print("pi:" + nextTimeString)
        ser.write(bytes(nextTimeString,"ascii"))
        ser.flush()

        while True:
            now = time.time()
            if now >= startTime + waitMax:
                return False
            data = ser.read(1)
            # print(data)
            if data != b'':
                if chr(data[0]) == "\n":
                    break
                message.append(chr(data[0]))
       
        message_string = "".join(message)
        print("f:" + message_string)
        if message_string == "success":
            return True


ser = serial.Serial('/dev/ttyAMA1',timeout = 1)  # open serial port
while True:
    startTime = time.time()
    print("start:" + str(startTime))
    try:
        if handshake() is False:
            resetFeather()
            continue
        success = negotiateNextTime()
        if success is True:
            break
        
    except ValueError:
        print("error, continuing to try again")
        continue
ser.close()             # close port
