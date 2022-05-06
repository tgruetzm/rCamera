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
  SOC = 36.4*battV-357 #estimate for SOC
  if(battV < 10.0):
   SOC = 0
  print("Battery {:>3.0f}% {:>5.3f} v".format(SOC, battV))
  time.sleep(0.5)
