import MainLibPython

dateTimeHelper = MainLibPython.DateTimeHelper()
d = dateTimeHelper.datetime_timestamp('2012-03-28 06:53:40')
print(d)
s = dateTimeHelper.timestamp_datetime(1332888820)
print(s)
