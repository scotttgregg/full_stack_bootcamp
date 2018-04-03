# rock_paper_scissors.py

import random

computer_list = ["rock", "paper", "scissors"]
user_list = ["rock", "paper", "scissors"]

def play_again():
    keep_playing = input('Would you like to play again?').lower()
    if keep_playing[0] == 'y':
        play_game()
    else:
        print("See ya!")

def play_game():
    user_choice = input("Choose 'rock', 'paper', or 'scissors'\n")
    while user_choice not in user_list:
        user_choice = input("Choose 'rock', 'paper', or 'scissors'\n")
    computer_choice = random.choice(computer_list)
    print("The computer chose " + computer_choice + ".")
    if computer_choice == user_choice:
        print("It's a tie.")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You win.")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Computer wins.")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Computer wins.")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You win.")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Computer wins.")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You win.")
    play_again()



play_game()
