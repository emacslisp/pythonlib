
# -*- coding: utf-8 -*-
 
import time
 
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt
 
def datetime_timestamp(dt):
     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
     return int(s)
 
if __name__ == '__main__':
    d = datetime_timestamp('2012-03-28 06:53:40')
    print(d)
    s = timestamp_datetime(1332888820)
    print(s)
