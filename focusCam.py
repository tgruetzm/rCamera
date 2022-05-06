#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

GPIO.output(27, GPIO.HIGH)
time.sleep(.5)
GPIO.output(27, GPIO.LOW)
time.sleep(.5)
  
