import time

contacts = {}
options = ['Create Contact', 'View Contact', 'Update Contact',
           'Delete Contact', 'Search Contact', 'Count Contacts', 'Exit']


def verifyName():
    name = input('Enter contact name: ')
    if name in contacts:
        return name
    else:
        return False


while True:
    time.sleep(1.5)
    print('\nCONTACH BOOK APP:\n')
    for i, opt in enumerate(options):
        print(f'{i+1}. {opt}')
    print()
    choice = int(input('Enter your choice: '))
    time.sleep(1)
    match choice:
        case 1:
            name = input('Enter contact name: ')
            if name in contacts:
                print(f'{name} already exists.')
            else:
                age = int(input('Enter age: '))
                email = input('Enter email: ')
                mobile = input('Enter mobile number: ')
                contacts[name] = {'age': age, 'email': email, 'mobile': mobile}
                print('Contact added.')
        case 2:
            print('Here is the list of contacts: ')
            for name in contacts.keys():
                print(name)
        case 3:
            name = input('Enter contact name: ')
            if name in contacts:
                age = int(input('Enter age: '))
                email = input('Enter email: ')
                mobile = input('Enter mobile number: ')
                contacts[name] = {'age': age, 'email': email, 'mobile': mobile}
            else:
                print(f'{name} does not exist.')
        case 4:
            name = input('Enter contact name: ')
            if name not in contacts:
                print(f'{name} does not exist.')
            else:
                del contacts[name]
                print(f'{name} deleted from contacts.')
        case 5:
            name = input('Enter contact name: ')
            if name in contacts:
                print(
                    f'Name: {name} \nAge: {contacts[name]['age']} \nE-mail: {contacts[name]['email']} \nMobile Nubmer: {contacts[name]['mobile']}')
            else:
                print(f'{name} does not exist')
        case 6:
            print(f'Number of contacts: {len(contacts)}')
        case 7:
            break
