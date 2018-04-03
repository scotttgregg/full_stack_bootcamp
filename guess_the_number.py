# Guess_the_number.py
import random


# use random.randit() and assign it to variable x
x = random.randint(1,10)
# print(x) # for testing purposes

# start a counter at 0
count = 0

# while True, run this
    # have user input a number and change it to an int()
    # if statement if user_guess is equal to x
        # print x
        # print statement to user telling them something
    # elif statement - elif count == 9 (meaning it looped 10 times)
        # print fail statement
        # break
    # else if user_guess is not equal to x
        # print guess again
        # add 1 to counter
while True:
    user_guess = int(input('Guess a number between 1 and 10: \n'))
    if user_guess == x:
        print('The computer guessed ' + str(x))
        print('You guessed it correctly! \n')
        break
    elif count == 9:
        print('Sorry, you failed to guess correctly!\n')
        break
    else:
        print('Sorry, guess again!\n')
        count += 1
