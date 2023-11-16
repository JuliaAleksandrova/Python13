import itertools

#counter = itertools.count()

# print(list(zip([10, 20, 30, 40], counter)))
#
# data = [100, 200, 300, 400, 500]
# data2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

#print(list(itertools.zip_longest(data, data2)))


#counter = itertools.count(start=1.5, step=0.5)
# data2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
# counter = itertools.cycle([1, 2, 3])
# print(list(zip(data2,counter)))
# counter = itertools.repeat(3, times=4)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
names = ['Jack', 'Mary']
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]

# result = itertools.compress(letters, numbers)
# print(list(result))
#
# result = itertools.filterfalse(lambda x: x > 2, numbers2)
# print(list(result))
# result2 = filter(lambda  x: x > 2, numbers2)
# print(list(result2))

# result = itertools.dropwhile(lambda x: x > 2, numbers2)
# result = itertools.takewhile(lambda x: x > 2, numbers2)
# print(list(result))
# result = itertools.accumulate(numbers2)
# print(list(result))
# no order no repeat
# result = itertools.combinations(range(10), 3)
# print(len(list(result)))
# for c in result:
#     print(c)

# result = itertools.permutations(letters, 4)
# # order, no repeat
# for c in result:
#     print(c)
#result = itertools.product(letters, numbers, repeat=4)
#order, repeat
# for c in result:
#     print(c)
# result = itertools.combinations_with_replacement(letters,4)
# #no order, repeat
# for c in result:
#     print(c)

import itertools



people = [
    {
        'name': 'John Smith',
        'city': 'Berlin'
    },
    {
        'name': 'Mary Gold',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi Tamm',
        'city': 'Berlin'
    },
    {
        'name': 'Piere Cardin',
        'city': 'Tallinn'
    },
    {
        'name': 'Jack Rock',
        'city': 'Tallinn'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul Faruh',
        'city': 'Dubai'
    },
    {
        'name': 'Mary Pierce',
        'city': 'Dubai'
    },
{
        'name': 'Lee Hong',
        'city': 'Tallinn'
    }
]
people.sort(key=lambda x: x['city'])
result = itertools.groupby(people, lambda x: x['city'])
for key, group in result:
    #print(key, result)
    print(list(group))




