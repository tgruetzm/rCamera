import board
import busio
import time
import rtc
import alarm
from adafruit_datetime import datetime
uart = busio.UART(board.TX, board.RX, baudrate=9600)

def handshake():
    message = []
    while True:
        now = time.time()
        if now >= startTime + waitMax:
            return False

        data = uart.read(1)
        # print(data)
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
        print("f:" + "send next time")
        uart.write(bytes("send next time\n", "ascii"))

def negotiateTime():
    validTime = False
    while validTime is False:
        nextTime = []
        while True:
            now = time.time()
            if now >= startTime + waitMax:
                return False
            data = uart.read(1)
            # print(data)
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
            print("f:" + "ack")
            uart.write(bytes("ack\n", "ascii"))
            validTime = True
            alarm.exit_and_deep_sleep_until_alarms(alarmT)
        except ValueError:
            print("Value Error: past time")
            print("f:" + "send next time")
            uart.write(bytes("send next time\n", "ascii"))

#start main processing
# set time UTC
r = rtc.RTC()
current_time = r.datetime
print(current_time)

waitMax = 7  # seconds

while True:
    startTime = time.time()
    print("restart:" + str(startTime))
    if handshake() is False:
        continue
    if negotiateTime() is False:
        continue
