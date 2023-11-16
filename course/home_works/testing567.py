#first_name, last_name, age  = input('Enter name, surname and age. Use "." as separator').split()
test = input().split()
print(test)





# #5
# set1 = (1, 2, 3, 5, 8)
# set2 = (8,2,5)
# set3 = set1[:2] + set2 + set1[2:]t
# print(set3)

#6
# list1 = [1, 1, 1, 1, 2, 4, 6, 4, 6, 6, 6]
# list2 = []
# for number in list1:
#     if list1.count(number) >= 2 and number not in list2:
#         list2.append(number)
# print(list2)

#7
# seconds = 1234565
# days = int(seconds/3600/24)
# hours = (seconds - days*24*3600)//3600
# minutes = (seconds - days*24*3600 - hours * 3600)//60
# seconds1 = seconds - days*24*3600 - hours * 3600 - minutes * 60
# print(f'{days}:{hours}:{minutes}:{seconds1}')