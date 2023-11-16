import re

# 1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
# 	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.
#([0-9A-Fa-f]{6})

# text = '#KLS323, #423abc, #AABBPP, #AAABBBCCCC'
# hex_color = re.compile(r'#[0-9a-fA-F]{6}\b')
# matches = re.finditer(hex_color, text)
# for match in matches:
#     print(match)
# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)
text = '''
2*9-6*5
(3+5)-9*4
# '''
#
# plus_numbers = re.compile(r'\d[^+]|\d')
# matches = re.finditer(plus_numbers, text)
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d+(?!\+)')
# search = pattern.findall(text)
# print(search)

# 3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время. [00:00 - 23:59]
text1 = '''
Завтрак в 09:00
'''
# time_pattern = re.compile(r'\b([01]\d|2[0-3]):([0-5]\d)\b')

# matches = re.finditer(time_pattern, text1)
# for match in matches:
#     print(match)
# pattern = r'(0[0-9]|1[0-9]|2[0-3]:[0-5][0-9])'
# matches = re.finditer(pattern, text1)
# for match in matches:
#     print(match.group())

# 4. Написать программу котороая будет выбирать из файла people.txt:
# 	1) Все имена и фамилии
# 	2) Все адреса

# name_pattern = re.compile(r'[A-Za-z-]+ [A-Za-z-]+\n')
# address_pattern = re.compile(r'\d{3} [A-Za-z0-9-]+ St\., [A-Za-z- \']+ [A-Z]{2} \d{5}')
# with open('people.txt', 'r') as file:
#     data = file.read()


# people_matches = re.findall(name_pattern, data)
# address_matches = re.findall(address_pattern, data)
# print(len(people_matches))
# for person in people_matches:
#     print(person)
# address_matches = re.findall(address_pattern, data)
# print(len(address_matches))

# 5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0
#^[a-zA-Z0-9]+$
# illegal_symbols = re.compile(r'[A-Za-z0-9]+')

matches = re.findall(illegal_symbols, text1)
# if matches:
#     print('NOK')
# else:
#     print('OK')
# if len(matches) == len(text):
#     print('OK')
# else:
#     print('Not ok')
# for match in matches:
#     print(match.group())
# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)
# pattern = r'^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{4}$'

idcode = re.compile(r'[1-8]\d\d(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
# Все строки произвольные.