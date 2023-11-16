user_input = input('Please enter ID code: ')
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
list_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
number_1 = 0
for i in range(10):
    number_1 += int(user_input[i]) * list_1[i]
    number_2 = number_1 % 11
if number_2  == int(user_input[10]):
    print('Your ID code is valid 1')
else:
    number_1 = 0
    for i in range(10):
        number_1 += int(user_input[i]) * list_2[i]
        number_2 = number_1 % 11
        if number_2 == int(user_input[10]):
            print('Your ID code is valid 2')



#     for i in range(10):
#         number_1 += int(user_input[i]) * list_2[i]
#         number_2 = number_1 % 11
#     if number_2 == int(user_input[10]):
#         print('Your ID code is valid')

# user_input = input('Please enter ID code: ')
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# list_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
# number_1 = 0
# if number_2  == int(user_input[10]):
#     for i in range(10):
#         number_1 += int(user_input[i]) * list_1[i]
#         number_2 = number_1 % 11
#     print('Your ID code is valid')

# 38803160272





