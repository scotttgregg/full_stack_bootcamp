# simple_calculator.py

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y




while True:
    user_operation = input(
                        'What is the operation you would like to perform?\n'
                        )
    if user_operation == '+':
        user_first_number = int(input('What is the first number?\n'))
        user_sec_number = int(input('What is the second number?\n'))
        print(
            str(user_first_number) + str(user_operation) + str(
                user_sec_number) + '=' + str(addition(
                user_first_number, user_sec_number))
                )
    elif user_operation == '-':
        user_first_number = int(input('What is the first number?\n'))
        user_sec_number = int(input('What is the second number?\n'))
        print(
            str(user_first_number) + str(user_operation) + str(
                user_sec_number) + '=' + str(subtract(
                user_first_number, user_sec_number))
                )
    elif user_operation == '*':
        user_first_number = int(input('What is the first number?\n'))
        user_sec_number = int(input('What is the second number?\n'))
        print(
            str(user_first_number) + str(user_operation) + str(
                user_sec_number) + '=' + str(multiply(
                user_first_number, user_sec_number))
                )
    elif user_operation == '/':
        user_first_number = int(input('What is the first number?\n'))
        user_sec_number = int(input('What is the second number?\n'))
        print(
            str(user_first_number) + str(user_operation) + str(
                user_sec_number) + '=' + str(divide(
                user_first_number, user_sec_number))
                )
    elif user_operation == 'done':
        break
