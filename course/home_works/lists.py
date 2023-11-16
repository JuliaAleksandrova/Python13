# 1
# Напишите программу которая сложит все числа в заданном списке
# выведет результат в консоль
nums1 = [5, 6, 92, 47, 12, -18, 33, 8];
sum = 0
for number in nums1:
    sum += number
print(sum)

# 2
# Напишите программу которая добавит в список edited_names словари
# с двумя парами { "name": "имя с большой буквы", "nameLength": "длина имени"}
names = ['jack', 'sarah', 'mary', 'joey', 'chris', 'samantha'];
edited_names = [];
for name in names:
    result = { "name": name.title(), "nameLength": len(name)}
    edited_names.append(result)
    for result in edited_names:
        print(result)


# 3
# Напишите программу которая в список edited_nums добавит словари
# с тремя парами { "number": "само число", "square": "число в квадрпате", "cube": "число в кубе"}
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
edited_nums = [];
for number in nums2:
    result = { "number": number, "square": number ** 2, "cube": number ** 3}
    edited_nums.append(result)
    for result in edited_nums:
        print(result)
# 4
# напишите программу которая выводит в консоль сумму всех
# четных чисел в списке

nums_list = [1, 12, 34, 71, 14, 12, 33, 70, 82, 81, 9, 19, 90];
sum = 0
for number in nums_list:
    if number % 2 == 0:
        sum += number
print(sum)


# 5
# напишите программу которая проанализирует данный список и выведет в консоль самую длинную строку

some_strings = ['Star', 'Planet', 'Comet', 'Interstellar', 'Space'];
longest_string = ''
for string in some_strings:
    if len(string) > len(longest_string):
        longest_string = string
        print(longest_string)

# 6
# напишите программу которая возьмёт из данного списка наименования книг которые вышли в этом году
# и добавит их в новый список

books = [
    {
        'author': 'Jeremy Brook',
        'title': 'My childhood',
        'release': 2023
    },
    {
        'author': 'Samantha Jhones',
        'title': 'Living with ten cats',
        'release': 2020
    },
    {
        'author': 'Bob Summers',
        'title': 'Exploring far space',
        'release': 2021
    },
    {
        'author': 'Bill Brown',
        'title': 'Insects in our garden',
        'release': 2023
    },
    {
        'author': 'Jessica Love',
        'title': 'Programming for begginers',
        'release': 2023
    }
];
booklist2023 = []
for book in books:
    if book['release'] == 2023:
        booklist2023.append(book)
print(booklist2023)

# 7
# Напишите функцию которая будет принимать два аргумента (start, end)
# Для каждого числа в диапозоне от start до end будет выводить число
# И Четное оно Или нечетное
def print_odd_or_even(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(f'{number} is odd.')
        else:
            print(f'{number} is even.')
start = 1
end = 10
print_odd_or_even(start, end)

