// # imports random thingy
// import random
//
// # make a list of responses
// eight_ball_response = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, dumb-dumb", "Most likely", "Outlook good", "Hell no", "No way", "Don't count on it", "Fuck no!"]
//
// # print welcome message
// def welcome_message():
//     print("Welcome to the Magic Eight Ball Program!")
//
// # input tell the user to ask a question to the magic Ball
//
// def ask_question_get_response():
//     input("Ask the Magic 8 Ball a question!\n")
//     print(random.choice(eight_ball_response))
//
// def play_again():
//     ask_second = input("Would you like to ask another question?\n")
//     while True:
//         if ask_second[0] == "y":
//             input("Ask Away!\n")
//             print(random.choice(eight_ball_response))
//             ask_second = input("Would you like to ask another question?")
//         else:
//             print("Thanks for playing!")
//             break
//
// welcome_message()
// ask_question_get_response()
// play_again()

let eightBallResponse = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, dumb-dumb", "Most likely",
                            "Outlook good", "Hell no", "No way", "Don't count on it", "Fuck no!"]

prompt("Ask the magic eight ball a question")
console.log(eightBallResponse[Math.floor(Math.random()*eightBallResponse.length)])