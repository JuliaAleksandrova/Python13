# 1. Create a program that generates a list of even numbers from 1 to 20 using a for loop.
list1 = []
for number in range(1, 21):
    if number % 2 ==0:
        list1.append(number)
print(list1)
# 2. Sum of List Elements: Create a function that calculates the sum of all elements in a list.

list2 = [34, 56, 78, 90]
sum2 = 0
for number in list2:
    sum2 += number
print(sum2)


# 3. Generate a list of squares for numbers from 1 to 10 using list comprehension.
list3 = []
for number in range(1, 11):
    square = number ** 2
    list3.append(square)
print(list3)

numbers = range(1, 11)
squares = [x ** 2 for x in numbers]
print(squares)

# 4. Count Vowels: Write a function that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string using a for loop and an if statement.

def check_vowels():
    word = input('Please enter Your word: ')
    word = word.lower()
    vowels = 'aeiou'
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    print(f'In your word is {vowel_count} vowels')

check_vowels()


# 5. Dictionary from Lists: Create a dictionary where keys are names and values are ages. You have two lists: one with names and the other with ages.
list_names = ['James', 'Samantha', 'Samuel', 'Ron']
list_ages = [33, 28, 45, 20]
list_na = {}
for name in range(len(list_names)):
    list_na[list_names[name]] = list_ages[name]
print(list_na)

# 6. Sort a Dictionary: Write a program to sort a dictionary by its values in ascending order.
list_nu = [3, 6, 8, 2, 5, 1, 56]
list_nu1 = sorted(list_nu)
print(list_nu1)

