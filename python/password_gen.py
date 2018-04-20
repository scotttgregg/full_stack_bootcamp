# password_gen.py

import random

# def too_short():
#     print('You must choose a minimum of 8 characters')
#     length = int(input('How many charaters would you like your password to be?: '))
#
# def print_welcome():
#     print('This is a password generator!')
#     print('Remember, a strong password should contain at least 8 characters')
#
# def length_and_create():
#     characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_&%$#@!'
#     password = ''
#     length = int(input('How many charaters would you like your password to be?: '))
#     if length < 8:
#         too_short()
#     for i in range(length):
#         password = password + random.choice(characters)
#     print(password)
#
# print_welcome()
# length_and_create()
#___________________________________________________________________________
# Version 3

def too_short():
    print('You must choose a minimum of 8 characters')
    length = int(input(
        'How many charaters would you like your password to be?: '))

def print_welcome():
    print('This is a password generator!')
    print('Remember, a strong password should contain at least 8 characters')

def length_and_create():
    upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_char = 'abcdefghijklmnopqrstuvwxyz'
    special_char = '!@#$%^&*()_-'
    num = '1234567890'
    password = ''
    length = int(input(
        'How many charaters would you like your password to be?: '))
    if length < 8:
        too_short()
    for i in range(length):
        random_choice = random.choice(
            upper_char + lower_char + special_char + num
            )
        password += random_choice
    print(password)

print_welcome()
length_and_create()
