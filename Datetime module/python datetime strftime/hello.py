from datetime import datetime
now=datetime.now()
year=now.strftime("%Y")
month=now.strftime("%m")
day=now.strftime("%d")
Time=now.strftime("%H:%M:%S")
fulldate=now.strftime("%d/%m/%Y %H:%M:%S")
print(now)
print(year)
print(month)
print(day)
print(Time)
print(fulldate)
print(now.strftime("%A"))
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))
#2023-07-04 10:29:34.342451
#2023
#07
#04
#10:46:40
#04/07/2023 10:46:40
#Tuesday
#Tue Jul  4 10:51:52 2023
#07/04/23
#10:51:52