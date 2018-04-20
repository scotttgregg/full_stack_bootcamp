# emoticon.py

import random
# set the count = 0 for the while loop
count = 0
# make lists for eyes, nose, and mouth
eyes = [':', ';', '8', '=', 'B', 'x']
nose = ['^', '-',]
mouth = [')', '(', 'D', 'P', 'X',]

# create function that prints concatination of random.choice(with each list name here)
def emoticon():
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

# creae while loop - while count is less than 5
# add an incrememnt of 1 to count - count += 1
# call emoticon funcion in while loop to print 5 emoticons
while count < 5:
    count += 1
    emoticon()
