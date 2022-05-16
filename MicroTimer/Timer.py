import datetime
from suntime import Sun, SunTimeException
from datetime import datetime, date, time, timedelta, timezone

latitude = 46.75
longitude = -114.08

sun = Sun(latitude, longitude)

today = datetime.now()
# Get today's sunrise and sunset
sr = sun.get_local_sunrise_time(today)
ss = sun.get_local_sunset_time(today)

tomorrow = today + timedelta(days = 1)

sunrise = datetime(tomorrow.year, tomorrow.month, tomorrow.day,sr.hour, sr.minute,  tzinfo=timezone(timedelta(hours =-6)))
sunset = datetime(tomorrow.year, tomorrow.month, tomorrow.day,ss.hour, ss.minute,  tzinfo=timezone(timedelta(hours =-6)))

sunriseTimes = [-20,-10,0,10,20,30]
sunsetTimes = [-30,-20,-10,0,10,20]

timeList = []

for t in sunriseTimes:
  t1 = sunrise + timedelta(minutes = t)
  timeList.append(t1)   

for t in sunsetTimes:
  t1 = sunset + timedelta(minutes = t)
  timeList.append(t1)  
