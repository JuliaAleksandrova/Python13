def id_code():
    global user_input
    while True:
        user_input = input('Please enter ID code or type "exit": ')
        if user_input.lower() == 'exit':
            break
        try:
            int(user_input)
            if len(user_input) != 11:
                raise UserWarning
        except ValueError:
            print('ID code is not numeric!')
        except UserWarning:
            if len(user_input) > 11:
                print('Code is too long!')
            else:
                print('Code is too short!')
        else:
            id_code = user_input
            break


def gender():
    if user_input[0] not in '09':
        if int(user_input[0]) % 2 == 0:
            print('You are female!')
        else:
            print('You are male!')

def date_of_birth():
    if user_input[0] not in '02':
        if int(user_input[0]) > 6:
            print(f' Date of birth: {user_input[5:7]}.{user_input[3:5]}.21{user_input[1:3]}')
        elif int(user_input[0]) > 4:
            print(f' Date of birth: {user_input[5:7]}.{user_input[3:5]}.20{user_input[1:3]}')
        elif int(user_input[0]) > 2:
            print(f' Date of birth: {user_input[5:7]}.{user_input[3:5]}.19{user_input[1:3]}')
        else:
            print(f' Date of birth: {user_input[5:7]}.{user_input[3:5]}.18{user_input[1:3]}')


def region():
    if int(user_input[7:10]) in range(1, 11):
        print('Kuressaare haigla')
    elif int(user_input[7:10]) in range(11, 20):
        print('Tartu Ülikooli Naistekliinik')
    elif int(user_input[7:10]) in range(21, 151):
        print(' Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja')
    elif int(user_input[7:10]) in range(151, 161):
        print('Keila haigla')
    elif int(user_input[7:10]) in range(161, 221):
        print('Rapla haigla, Loksa haigla, Hiiumaa haigla')
    elif int(user_input[7:10]) in range(221, 271):
        print(' Ida-Viru keskhaigla')
    elif int(user_input[7:10]) in range(271, 371):
        print('Maarjamõisa kliinikum')
    elif int(user_input[7:10]) in range(371, 421):
        print('Narva haigla')
    elif int(user_input[7:10]) in range(421, 471):
        print('Pärnu haigla')
    elif int(user_input[7:10]) in range(471, 491):
        print('Haapsalu haigla')
    elif int(user_input[7:10]) in range(491, 521):
        print('Järvamaa haigla')
    elif int(user_input[7:10]) in range(521, 571):
        print('Rakvere haigla')
    elif int(user_input[7:10]) in range(571, 601):
        print('Valga haigla')
    elif int(user_input[7:10]) in range(601, 651):
        print('Viljandi haigla')
    elif int(user_input[7:10]) in range(651, 701):
        print('Lõuna-Eesti haigla')
    else:
        print('You are not born in Estonia')


def validation():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    for num in range(len(chk1)):
        result += chk1[num] * int(user_input[num])
    if int(user_input[-1]) == result % 11:
        print('Code is valid! 1')
    else:
        result = 0
        for num in range(len(chk2)):
            result += chk2[num] * int(user_input[num])
        if int(user_input[-1]) == result % 11:
            print('Code is valid! 2')
        else:
            print('Code is not valid!')


def options():
    while True:
        user_choice = input('Please choose:\n'
                            '1.Gender\n'
                            '2.Date of birth\n'  # dd.mm.yyyy
                            '3.Region\n'
                            '4.Validate\n'
                            '5.Change ID\n'
                            '0.Exit\n'
                            '-->')
        if user_choice == '1':
            print(gender())
        elif user_choice == '2':
            print(date_of_birth())
        elif user_choice == '3':
            print(region())
        elif user_choice == '4':
            print(validation())
        elif user_choice == '5':
            print(id_code())
        elif user_choice == '0':
            break


id_code()
options()

