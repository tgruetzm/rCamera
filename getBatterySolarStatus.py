import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
#chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
battChan = AnalogIn(ads, ADS.P0, ADS.P1)

solarChan = AnalogIn(ads, ADS.P2, ADS.P3)


while True:
  battV = battChan.voltage *8
  SOC = 0
  range = .1

  if(battV >= 12.6-range):
    SOC = 100
  elif(battV >=12.3-range):
    SOC = 92
  elif(battV >=12.0-range):
    SOC = 80
  elif(battV >=11.7-range):
    SOC = 72
  elif(battV >=11.4-range):
    SOC = 60
  elif(battV >=11.1-range):
    SOC = 50
  elif(battV >=10.8-range):
    SOC = 33
  elif(battV >=10.5-range):
    SOC = 17
  elif(battV >=10.2-range):
    SOC = 8
  elif(battV >=9.9-range):
    SOC = 5
  elif(battV >=9.6-range):
    SOC = 0

  print("Battery {:>3}% {:>5.3f} v".format(SOC, battV))
  time.sleep(0.5)
