"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import datetime

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'
d1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(d1)
print(type(d1))
d2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(d2)
print(type(d2))
d3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(d3)
print(type(d3))
d4 = datetime.datetime.strptime(sample4, '%m.%d.%Y - %H:%M:%S')
print(d4)
print(type(d4))


# Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(f'Yesterday: {yesterday}, today: {today}, tomorrow: {tomorrow}')


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
date = datetime.datetime.fromtimestamp(some_day).strftime('%d.%m.%y')
print(f'Converted date:{date}')


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
from datetime import datetime, timedelta
def sub_two_weeks(timestamp):
    new_timestamp = timestamp - 2 * 7 * 24 * 3600
    return new_timestamp

input_timestamp = 1698325469
new_timestamp = sub_two_weeks(input_timestamp)
print("Input:", input_timestamp)
print("Output:", new_timestamp)