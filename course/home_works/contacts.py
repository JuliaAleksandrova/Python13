# contacts_book = {}
# def add_contact():
#     name = input('Enter Your name: ')
#     phone = input('Enter Your phone nr: ')
#     email = input('Enter Your email: ')
#     contacts_book[name] = {'phone': phone, 'email': email}
#     print(f' Contact {name} was added!')
#
# def view_contact(name):
#     if name in contacts_book:
#         contact = contacts_book[name]
#         print(f"Name: {name}, phone nr: {contact['phone']}, email: {contact['email']}")
#     else:
#         print(f'Contact is not found.')
#
# def delete_contact(name):
#     if name in contacts_book:
#         del contacts_book[name]
#         print(f'Contact {name} was deleted')
#     else:
#         print(f'Contact is not found.')
#
#
# def update_contact(name):
#     if name in contacts_book:
#         phone = input('Please enter new phone nr: ')
#         email = input('Please enter new email: ')
#         contacts_book[name] = {'Phone nr': phone, 'email': email}
#         print(f'Contact {name} was updated')
#     else:
#         print(f'Contact is not found.')
#
#
# add_contact()
# print(contacts_book)
# view_contact('ju')
# update_contact('ju')
# delete_contact('ju')
#
contact_book = {}
def add_contact(name, phone, email):
    if name not in contact_book:        #name eto peremennaja poetomu bez skobok
        contact_book[name] = {
            'phone': phone,
            'email': email
        }
        print(f'Contact {name} was successfully added')
    else:
        print(f'Contact {name} already exists')


def view_contact(name):
    if name in contact_book:
        contacts = contact_book[name]
        #contact_book[name]['phone']
        print(f'Name {name}, Phone: {contacts["phone"]}, email: {contacts["email"]}')
    else:
        print(f'Contact {name} does not exist.')


def update_contact(name, phone, email):
    if name in contact_book:
        #contact_book[name] = {'phone': phone, 'email': email}
        #contact_book[name].update({'phone': phone, 'email': email})
        contact_book.update({name: {'phone': phone, 'email': email}})
        print(f'Contact {name} was successfully added')
    else:
        print(f'Contact {name} does not exist')

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f'Contact {name} was deleted')
    else:
        print(f'Contact {name} does not exist')



add_contact('Julia', 1, 1)

update_contact('Julia', 2, 2)
view_contact('Julia')


