#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta


# 方法一
# 计算两个日期之间的差值，默认单位为天，可以指定为月或年
def datediff(date1, date2, unit='d'):
    if unit == 'd':
        return (date2 - date1).days
    elif unit == 'm':
        return (date2.year - date1.year) * 12 + date2.month - date1.month
    elif unit == 'y':
        return date2.year - date1.year
    else:
        return None


print(datediff(datetime(2020, 1, 1, 0, 0, 0), datetime.now(), 'd'))
print(datediff(datetime(2020, 1,  1, 0, 0, 0), datetime.now(), 'm'))
print(datediff(datetime(2020, 1, 1, 0, 0, 0), datetime.now(), 'y'))


# 方法二
# 根据是否为闰年，返回月份的天数
def is_leap(year):
    normal = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    leap = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return leap
    else:
        return normal

# 计算两个日期之间的差值，默认单位为天，可以指定为月或年
def datediff2(date1, date2, unit='d'):
    days = 0
    if unit == 'd':
        if date1.year == date2.year:
            month = is_leap(date1.year)
            for i in range(date1.month, date2.month):
                days += month[str(i)]
        elif date1.year == date2.year - 1:
            month1 = is_leap(date1.year)
            month2 = is_leap(date2.year)
            for i in range(date1.month, 13):
                days += month1[str(i)]
            for i in range(1, date2.month):
                days += month2[str(i)]
        else:
            month1 = is_leap(date1.year)
            month2 = is_leap(date2.year)
            for i in range(date1.month, 13):
                days += month1[str(i)]
            for i in range(1, date2.month):
                days += month2[str(i)]
            for i in range(date1.year + 1, date2.year):
                if is_leap(i):
                    days += 366
                else:
                    days += 365
        return days - date1.day + date2.day
    elif unit == 'm':
        return (date2.year - date1.year) * 12 + date2.month - date1.month
    elif unit == 'y':
        return date2.year - date1.year
    else:
        print('unit must be d, m or y')


# 测试数据
database = [
    [[datetime(2000, 2, 7), datetime(2000, 2, 7)], 0],
    [[datetime(2000, 2, 7), datetime(2000, 2, 8)], 1],
    [[datetime(2000, 2, 1), datetime(2000, 3, 1)], 29],
    [[datetime(1999, 2, 7), datetime(2024, 10, 8)], 9375]
]
for date in database:
    print(datediff2(date[0][0], date[0][1], 'd') == date[1], date[0][1] - date[0][0])
