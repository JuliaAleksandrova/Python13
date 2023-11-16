string_sample1 = 'Hello world world'
string_sample2 = 'first leTter is loWercase. new-sentnce'
string_sample3 = '*  **extra symbols  '
german_sample = 'der fluß'
#metod len merit dlinu stroki
#esli nuzno uznat cislo simvolov u cista, nado konvertirovat v stoku, u stroki ono est
# print(len(string_sample1))
# print(type(len(string_sample1)))
# print(string_sample1[16]) #poprosila pokazat pervyj simvol, otscet s nulja indeksiruem stroku
# print(string_sample1[len(string_sample1) - 1])
#[start:end:step]
#0123456...
# -5-4-3-2
#stroka neizmenjaemyj tip dannyh
#print(string_sample1[0])
#print(string_sample1[-17])
#print(string_sample1[0:5]) #vytaskivaju slovo Hello, poslednee cislo ne vkljuceno
#print(string_sample1[0:5][0])
#print(string_sample1 )
# print(string_sample1[0:14:2]) #s nulevogo po 14 kazdaja vtoraja bukva
# print(string_sample1[-6:-1]) #diapozony otricatelnye tal
# print(string_sample1[-6:])
# print(string_sample1[::-1]) #razvoracivaet stroku
# print('Hello world '[::-1]) #razvoracivaet stroku
#
# #komentit mnogo strok cntr certocka
#
# print('world' in string_sample1) # vozvrawaet boulean
# print('a' > 'A')
# print('world' > 'planet') #sravnenie po ervoj bukve
# print(string_sample2.upper()) #vse bukvy zaglavnye
# print('Hello'.isupper()) #proverjaem vse li zaglavnye
# print(german_sample.lower().islower())
# print(german_sample.casefold()) #beret alternativu na latinicu
#
# print('HELLLO world'.swapcase()) #zamenil malenkie na bolshie
# print(string_sample2.capitalize()) #vse bukvy opuskaet krome pervoj
#
# print(string_sample2.title())
# print(string_sample2.istitle())
#
# print(string_sample3.strip('* ')) #vyrezaet probely s konca i s nacala
# print(string_sample1.replace('w', 'W')) #zamenjaet, vyrezaet
# print(string_sample1.replace('world', '', 1))
# print('Hello people, of planet Earth'.split(', ')) #razbivaet stroku na casti
# a, b, c, = input('Enter a, b, c: ').split()
# print(a, b, c)

# print(string_sample1.count('world', 0, 12)) #mozet poscitat skolko cego
# print(string_sample1.find('world')) #pokzyvaet gde nahoditsa stroka

# print('Hello', 'Planet', 123, sep='', end='\n') #cerez zapjatuju pishet, razdeljaet, mozno oboznacit cem
# print(len('Wor\nld'))
# print('World')
# print('That\'s it') #simvol esc
# print("My favourite book \"Harry Potter\"")
# print(r'\tHello\new')
name = 'John'
salary = 1000
age = 20
# salary_str = '{2}s salary is {1}. Age{0}{0}{0}' #
# print(salary_str.format(name, salary, age))

# salary_str = '{user_name}s salary is {user_salary:.2f}. Age{user_age}'#otobrazi float s dvumka ciframi
# print(salary_str.format(user_name=name, user_age=age,user_salary=salary))

print(f'{name}s salary is {salary:.2f}. He is {age} years old.') #formatirovanaja stroka
by
