import time
import calendar
tick=time.time()
print(tick)
localTime=time.asctime(time.localtime(time.time()))
print(localTime)
cal=calendar.month(1992,6)
print(cal)
print(time.altzone)
print(time.localtime())
print(time.strftime("%b %d %Y %H:%M:%S",time.localtime()))
