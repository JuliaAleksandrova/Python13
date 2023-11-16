# def squares_generator(start, end):
#     for num in range(start, end + 1):
#         yield num **2
#
# def infinite_counter(start):
#     while True:
#         start += 1
#         yield start -1
#
# y = infinite_counter(0)
# print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))


# x = squares_generator(1, 100)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# for i in x:
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def squares(number):
#     return number ** 2
# new_nums = map(squares, numbers)
#
# # new_nums = []
# # for num in numbers:
# #     new_nums.append(squares(num))
# print(list(new_nums))
# def change_dict(d):
#     make, model, serial = d['make'], d['model'], d['serial']
#     return {
#         serial:{
#             'make': make,
#             'model': model
#         }
#     }
#
# cars = [
#     {
#         'make': 'VW',
#         'model': 'Golf',
#         'serial': '2134dsasad131'
#
#     },
#     {
#         'make': 'BMW',
#         'model': '320i',
#         'serial': '2as1234dsvbd131'
#
#     },
#
#     {
#         'make': 'Seat',
#         'model': 'Leon',
#         'serial': 'sa23kmm322133'
#
#     }
# ]
# new_cars = map(change_dict,cars)
# print(list(new_cars))

# def power(a, b):
#     return a ** b
#
# nums = [1, 2, 3, 4, 5, 6]
# nums2 = [5, 6, 7, 8, 9, 10]
#
# new = map(power, nums, nums2)
# #print(list(new))
# print(sum(list(new)))
#
# nums = [1, 2, 3, 4, 5, 6]
# def odd_or_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# new = filter(odd_or_even, nums)
# print(list(new))

# data1 = [1, 2, 3, 4, 5]
# data2 = ['mon', 'tue', 'wed', 'thu', 'fri']
# new = zip(data1, data2)
# print(list(new))










