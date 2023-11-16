# Практикум 1:
#
# 1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#     Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>
# first_name, last_name, age  = input('Enter name, surname and age. Use "." as separator').split()
# print(f'Hello, {last_name} {first_name}. Your age is : {age}')
import math

# 2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам. (
# с = sqrt(a * a  +  b * b))
# a = 3
# b = 4
# c = (a**2 + b**2) ** 0.5
# c = math.sqrt(a**2 + b**2)
# print(c)



# 3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет, является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5
# a, b, c = input('Enter sides A, B and C: ').split()
# if float(c) ** 2 == float(a) ** 2 + float(b) ** 2:
#     print(True, 'This is right triangle')
# else:
#     print(False, 'This is not right triangle')



# 4 Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка в обратном порядке.


# user_list = input('Enter list elements: ').split(', ')
# user_list.reverse()
# for item in user_list:
#for item in user_list[::-1]:
#   print(item)



# 5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#     Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)
# a = (1, 2, 3, 5, 8)
# b = (8,2,5)
# a = a[:2] + b + a[2:]
# print(a)
# a = list(a)
# print(id(a))
# for num in b[::-1]:
#     a.insert(2,num)
# a = tuple(a)
# print(a)

# a = [1, 2, 3]
# print(id(a))
# a.append()
# print(id(a))
# 6 *Написать программу, которая для произвольного списка находит число / числа, наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.
#     Примеры:
#     [1, 2, 3, 4, 7, 9, 9] → [9]
#     [1, 2, 4, 6, 4, 6] → [4,6]

test_list = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10]
#print(test_list.count(8))
# max_count = 0
# result = []
# for num in test_list:
#     if test_list.count(num) > max_count:
#         max_count = test_list.count(num)
# for num in test_list:
#     if test_list.count(num) == max_count and num not in result:
#         result.append(num)
# print(result)
# result = {}
# for num in test_list:
#     result[num] = test_list.count(num)
# res = []
# for key in result.keys():
#     if result[key] == max(result.values()):
#         res.append(key)
# print(res)


#print(list(set(result)))
#
# 7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#     Примеры:
#     1234565 seconds = 14:6:56

# set1 = (1, 2, 3, 5, 8)
# set2 = (8,2,5)
# set3 = set1[:2] + set2 + set1[2:]
# print(set3)

#***
# list1 = list(set1)
# list2 = list(set2)
# set3 = list1[:2] + list2 + list1[2:]
# set4 = tuple(set3)
# print(set4)



# ***
# list1 = [1, 2, 4, 6, 4, 6]
# list2 = []
# for number in list1:
#     if list1.count(number) == 2 and number not in list2:
#         list2.append(number)
# print(list2)

# list1 = [1, 2, 4, 6, 4, 6]
# dublicates = []
# for item in list1:
#     if list1.count(item) == 2:
#         dublicates.append(item)
# print(dublicates)

#Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#     Примеры:
#1234565 seconds = 14:6:56

seconds = 1234565
# minutes = seconds/60
# hours = minutes/60
# days = hours/24
# days = int(seconds/3600/24)
# hours = (seconds - days*24*3600)//3600
# minutes = (seconds - days*24*3600 - hours * 3600)//60
# seconds1 = seconds - days*24*3600 - hours * 3600 - minutes * 60
# print(f'{days}:{hours}:{minutes}:{seconds1}')
# print(days)
# print(hours)
# print(minutes)
# print(seconds1)

days = seconds//(3600*24)
seconds %= 24 * 60 * 60
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{minutes}:{seconds}')

# hours = (seconds % (3600*24))//3600
# minutes = (seconds % 3600)//60
# seconds1 = seconds % 60
# print(f'{days}:{hours}:{minutes}:{seconds1}')










