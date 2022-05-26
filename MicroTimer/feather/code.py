import board
import busio
import time
import rtc
import alarm
import neopixel
from adafruit_datetime import datetime
from digitalio import DigitalInOut, Direction, Pull
uart = busio.UART(board.TX, board.RX, baudrate=9600)

def handshake():
    message = []
    while True:
        now = time.monotonic()
        if now >= startTime + waitMax:
            return False

        data = uart.read(1)
        #print(data)
        if data is not None:
            if chr(data[0]) == "\n":
                break
            message.append(chr(data[0]))

    message_string = "".join(message)
    if message_string.startswith("hello feather"):
        mArr = message_string.split(',')
        print("pi:" + message_string, end='\n')
        dt = datetime.fromisoformat(mArr[1])
        print("setting time")
        r.datetime = time.struct_time((dt.year, dt.month, dt.day, dt.hour, dt.minute,
        dt.second, 0, -1, -1))
        print(dt)
        print("f:" + "ack")
        uart.write(bytes("ack\n", "ascii"))
        print("f:" + "send next time")
        uart.write(bytes("send next time\n", "ascii"))
        return True

def negotiateTime():
    validTime = False
    while validTime is False:
        nextTime = []
        while True:

            now = time.monotonic()
            if now >= startTime + waitMax:
                return False
            data = uart.read(1)
            print(data)
            if data is not None:
                if chr(data[0]) == "\n":
                    break
                nextTime.append(chr(data[0]))

        alarmTime = "".join(nextTime)
        if alarmTime.startswith("hello feather"):
            return False
        print("alarmTime:" + alarmTime)
        at1 = alarmTime.split('.')
        # print(at1)
        at2 = int(at1[0])
        # print(at2)
        try:
            alarmT = alarm.time.TimeAlarm(epoch_time = at2)
            print("f:" + "success")
            uart.write(bytes("success\n", "ascii"))
            validTime = True
            led.brightness = 0
            alarm.exit_and_deep_sleep_until_alarms(alarmT)
        except ValueError:
            print("Value Error: past time")
            print("f:" + "send next time")
            uart.write(bytes("send next time\n", "ascii"))

def wakePi():
    print("waking pi")
    wakePin.value = True
    time.sleep(1)
    wakePin.value = False


#start main processing

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .01
led[0] = (0, 255, 0)

piActive = DigitalInOut(board.D10)
piActive.direction = Direction.INPUT
piActive.pull = Pull.UP


wakePin = DigitalInOut(board.D4)
wakePin.direction = Direction.OUTPUT


if piActive.value is False:
    wakePi()

# set time UTC
r = rtc.RTC()
current_time = r.datetime
print(current_time)

waitMax = 7  # seconds
waitAbsMax = 600 #600 seconds 10 minutes
wakeTime = time.monotonic()

while True:
    startTime = time.monotonic()
    print("restart:" + str(startTime))
    if startTime >= wakeTime + waitAbsMax:
        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 3600)#3600 seconds, 1 hour
        # something bad happend, go to sleep for 1 hour and retry
        alarm.exit_and_deep_sleep_until_alarms(time_alarm)
    if handshake() is False:
        continue
    if negotiateTime() is False:
        continue
