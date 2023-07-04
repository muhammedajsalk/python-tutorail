import datetime

now= datetime.datetime.now()
print(now)
#current time current date


date=datetime.date.today()
print(date)
#current date


date=datetime.date(2018,1,1)
print(date)
#Date construction


date=datetime.date.today()
print("Year : ",date.year)
print("Month : ",date.month)
print("Month : ",date.day)
#current year,month,day


now=datetime.time(10,10,10)
print(now)
print(now.hour)
print(now.minute)
print(now.second)
#10:10:10
#10
#10
#10


now=datetime.datetime(2022,4,1,10,10,10)
print(now)
#2022-04-01 10:10:10


from datetime import date
date1=date(2023,2,1)
date2=date(2021,9,1)
date3=date1-date2
print(date3)
#518 days, 0:00:00 diffrence