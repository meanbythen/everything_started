#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/06 21:08
# @Author  : meanbythen

import sys

weather_str = ''
with open('weather.txt', 'r', encoding='utf-8') as f:  # encoding='utf-8'指定编码格式
    weather_str = f.read()  # 读取文件内容，返回一个字符串,read()方法会读取文件的全部内容，并将其作为一个字符串返回,readline()方法可以一次读取一行内容,readlines()方法可以一次读取所有行内容，并返回一个列表
    print(type(weather_str))
    print(weather_str[:50])
# weather_list = [line.split(';') for line in weather_str]
weather_list = [i for i in weather_str.split(';')]  # 使用列表推导式将每一行字符串按';'分割成列表,split()方法可以按照指定的分隔符将字符串分割成多个子字符串，并返回一个列表
# weather_list = weather_str.split(";")
print(type(weather_list))
print(weather_list[:50])

weather_data = []
print(type(weather_data))
for data in weather_list:
    data = data.split(',')
    data = {
        'city': data[0],
        'date': data[1],
        'minTemp': int(data[2]),
        'maxTemp': int(data[3])
    }  # 将列表中的数据转换为字典.data作为临时变量，删除链接2次，重新赋值2次，直接在循环中完成
    weather_data.append(data)
print(f'共加载了{len(weather_data)}条数据')  # len()函数可以返回列表的长度，即列表中元素的个数
print(weather_data[:2])

count = 0
for data in weather_data:
    if data['city'] == '广州' and data['minTemp'] < 10 and data['date'].split('-')[0] == '2010':
        count += 1
print(f'广州2010年有{count}天最低气温低于0度')

count = 0
for data in weather_data:
    if data['city'] in ['广州', '深圳'] and data['maxTemp'] > 30 and data['date'].split('-')[0] == '2015':
        count += 1
print(f'广州和深圳2015年有{count}天最高气温超过30度')

search_data = []
for data in weather_data:
    if data['maxTemp'] > 35:
        search_data = data
        break
print(f'第一个最高温度超过35度的城市是{search_data['city']}')

search_cities = []
for data in weather_data:
    if data['city'] in search_cities:
        continue
    if data['maxTemp'] > 30 and data['date'].split('-')[1] == '10':  # data['date'].split('-')[1]表示将日期字符串按'-'分割成列表，取列表中的第二个元素，即月份,比较时注意字符串和整数的比较
        search_cities.append(data['city'])
print(f'10月最高温度超过30度的城市{'、'.join(search_cities)}')
