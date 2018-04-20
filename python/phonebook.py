# phonebook.py

phonebook = {'Emily': {'first name': 'Emily',
                        'last name': 'Schultz',
                        'number': '555-555-5555'},
            'Sara': {'first name': 'Sara',
                        'last name': 'Schultz',
                         'number': '555-555-5555'},
            'Eric': {'name': 'Eric',
                        'last name': 'Gregg',
                         'number': '555-555-5555'}}

def create_new():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    user_name = input("Enter username: ")
    phonebook[user_name] = {'firstname': first_name,
                            'lastname': last_name,
                            'number': phone,
                            'username': user_name}
    # print(phonebook)


def retrieve_contact():
    get_contact = input(
                        'Enter username of contact that you would like to view: '
                        )
    if get_contact in phonebook:
        print(phonebook[get_contact])
    else:
        print('There is no one by that name in your phonebook. ')


def update_contact():
    contact_update = input('What contact would you like to update?: ')
    if contact_update in phonebook:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        user_name = input("Enter username: ")
        dict1 = {
                'firstname': first_name,
                'lastname': last_name,
                'number': phone,
                'username': user_name
                }
        phonebook[contact_update].update(dict1)
    else:
        print('That name is not in your phonebook.')

def delete_contact():
    contact_delete = input('What contact would you like to delete?: ')
    if contact_delete in phonebook:
        del phonebook[contact_delete]
        print(phonebook)
    else:
        print('That name is not in your phonebook.')


def menu():
    print("To create new, type '1'. ")
    print("To retrieve a contact, type '2' ")
    print("To update a contact, type '3' ")
    print("To delete a contact, type '4' ")
    user_input = input(
        "Type the option number that you would like to complete.")
    if user_input == '1':
        create_new()
    elif user_input == '2':
        retrieve_contact()
    elif user_input == '3':
        update_contact()
    elif user_input == '4':
        delete_contact()


menu()
print(phonebook)
