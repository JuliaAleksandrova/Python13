# r- read
# a- append
# w - write
# x- create
# r+ - read and write

# file = open('lor.txt', 'r', encoding='UTF8')
# print(file.name)
# print(file.mode)
# print(file.encoding)
# file.close()
# print(file.closed)

# C:\Users\julie\PycharmProjects\pythonProject\Python13\course\working_with _files\lor.txt
# course/working_with _files/lor.txt

# with open('lor.txt', 'r', encoding='UTF8') as file:
#     file_content = file.read()
# print(file_content)
# print(type(file_content))
# file_content2 = file.read()
# print('******')
# print('******', file_content2)

#with open('lor.txt', 'r', encoding='UTF8') as file:
    #file_content = file.readlines()
    # file_content = file.readline()
    # print(len(file_content))
    # file_content = file.read(20)
    # print(file_content)
# print(file_content)
# print(type(file_content))
# print(len(file_content))

# for line in file_content:
#     print(line, end='')

# with open('lor.txt', 'r', encoding='UTF8') as file:
#     read_size = 100
#     file_content = file.read(read_size)
    #file.seek(500)

    # while len(file_content) > 0:
    #     print(file_content)
    #     file_content = file.read(read_size)
#
# with open('lor.copy.txt', 'w', encoding='UTF8') as file:
#      file. seek(0)
#      file.write('****')
#      file.write('Hi there\n')
#      file.write('Hello world\n')


# with open('lor.copy.txt', 'a', encoding='UTF8') as file:
#      file.write('Hi there\n')
#      file.write('Hello world\n')

# with open('lor.copy.txt', 'x', encoding='UTF8') as file:
#      file.write('Hi there\n')
#      file.write('Hello world\n')

# with open('lor.copy.txt', 'r+', encoding='UTF8') as file:
#      data = file.read().upper()
#      file.seek(0)
#      file.write(data)

with open('img.png', 'rb') as picture:
    data = picture.read()

with open('img_copy.png', 'wb') as picture_copy:
    picture_copy.write(data)

print(data)



















