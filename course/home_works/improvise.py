# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
#
# res = x + y
# res. sort()
# print(res)

# x += y
# x = list(x)
# x.sort()
# x = tuple(x)
# print(x)

# x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# y = (7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
#
# x_set = set(x)
# y_set = set(y)
#
# same = x_set.intersection(y_set)
# print(same)
# res = []
# for num in x + y:
#     if num in same:
#         res.append(num)
#
# res.sort()
# res = tuple(res)
# print(res)
def ask_question(q):
    print(q['question'])
    for i in range(1, 5):
        print(f'{i}.{q["answers"][i-1]}')

def get_answer():
    while True:
        user_answer = input('Answer nr.: ')
        if user_answer in ['1', '2', '3', '4']:
            return user_answer
        print('Try again!')


def play():
    global user_results
    for question in quiz.values():
        ask_question(question)
        answer = get_answer()
        user_answer = question['answers'][int(answer) - 1]
        if user_answer == question['correct_answer']:
            user_results += 1

    print(f'Your answered {user_results} question correctly!')


quiz = {
    'q1': {
        'question': 'What color sky is?',
        'answers': ['Red', 'Yellow', 'Green', 'Blue'],
        'correct_answer': 'Blue'
    },
    'q2': {
        'question': 'What color sun is?',
        'answers': ['Red', 'Yellow', 'Green', 'Blue'],
        'correct_answer': 'Yellow'
    },
    'q3': {
        'question': 'What color grass is?',
        'answers': ['Red', 'Yellow', 'Green', 'Blue'],
        'correct_answer': 'Green'
    },
}
user_results = 0
play()







