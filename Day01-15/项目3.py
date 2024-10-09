# 从外部文件读取数据
weather_str = ''
with open('weather.txt', 'r', encoding='utf-8') as f:
    weather_str = f.read()
# print(weather_str[0:50])


# 处理有规律的字符串
weather_list = weather_str.split(';')
weather_data = []
# print(weather_list[0:10])

for data in weather_list:
    data = data.split(',')
    data = {
        '城市': data[0],
        '日期': data[1],
        '最低温度': int(data[2]),
        '最高温度': int(data[3]),
    }
    
    weather_data.append(data)

print('共加载气象数据：', len(weather_data))
# print(weather_data[0:2])


# 广州在2010年中有多少天最低温度小于10度
count = 0
for data in weather_data:
    if data['城市'] == '广州' and data['最低温度'] < 10 and data['日期'].split('-')[0] == '2010':
        count += 1
print(f'广州2010年中有 {count} 天最低温度小于10度')


# 深圳和广州在2015年有多少天最高温度大于30度
count = 0
for data in weather_data:
    if (data['城市'] == '广州' or data['城市'] == '深圳') and data['最高温度'] > 30 and data['日期'].split('-')[0] == '2015':
        count += 1
print(f'深圳和广州在2015年中有 {count} 天最高温度超过30度')

# 另一种写法
# data['城市'] in ['广州', '深圳']


# 第一个最高温度超过35度的数据
search_data = {}
for data in weather_data:
    if data['最高温度'] > 35:
        search_data = data
        break
print('第一个最高温度超过35度的城市：', search_data['城市'])


# 所有10月最高温度超过30度的城市
search_cities = []
for data in weather_data:
    if data['城市'] in search_cities:
        continue
    if data['最高温度'] > 30 and data['日期'].split('-')[1] == '10':
        search_cities.append(data['城市'])
print('所有10月最高温度超过30度的城市：', '、'.join(search_cities))
