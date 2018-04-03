# palindrome_detector.py

user_input = input("Enter in a string to see if it's a palindrome:\n")

user_input = user_input.replace(' ', '')

reversed_input = user_input[::-1]

if reversed_input == user_input:
    print("It's a palindrome!\n")
else:
    print("Not a palindrome.")
