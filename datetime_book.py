import datetime

mytime = datetime.time(2, 20, 59, 20)

print(mytime.minute)

print(mytime.hour)

print(mytime.microsecond)

today = datetime.date.today()
print(today)
print(today.ctime())

from datetime import datetime

mydateTime = datetime(2021,10,3,14,20,1)
print(mydateTime)

mydateTime = mydateTime.replace(year=2020)
print(mydateTime)

from datetime import date
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

result = date1 - date2
print(type(result))

print(result.days)

print(result.seconds)

print(result.total_seconds())