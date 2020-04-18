# -*- coding: utf-8 -*-

#计算时间差的分钟数

# 同一天的时间差
from datetime import datetime, date

time_1 = '2020-03-02 15:00:00'
time_2 = '2020-03-02 16:00:00'

time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
seconds = (time_2_struct - time_1_struct).seconds
print('同一天的秒数为：%s' % seconds)


# 不同天的时间差
time_1 = '2020-03-02 15:00:00'
time_2 = '2020-03-03 16:00:00'

time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")

# 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分，没有包含天数差，total_seconds包含天数差
# 所以total_seconds两种情况都是可以用的
total_seconds = (time_2_struct - time_1_struct).total_seconds()
print('不同天的秒数为：')
print(int(total_seconds))

min_sub = total_seconds / 60
print('不同天的分钟数为：')
print(int(min_sub))

# 只有时间time没有日期时，求时间差先可以加上一个相同的日期，再求时间差
# date.min能表示的最小日期
# date.max能表示的最大日期
# date.today()返回一个当前日期对象
# datetime.combine：根据所给的date和time创建一个datetime对象
time_sub = datetime.combine(date.min, time_2_struct.time()) - datetime.combine(date.min, time_1_struct.time())
print('----- 与最小日期结合： ------')
print(time_sub.seconds/60)

time_sub = datetime.combine(date.today(), time_2_struct.time()) - datetime.combine(date.today(), time_1_struct.time())
print('----- 与当天日期结合： ------')
print(time_sub.seconds/60)
print(time_sub.total_seconds()/60)

