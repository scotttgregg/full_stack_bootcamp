# pick6.py

import random

def pick_6_randos():
    pick_6 = []
    for x in range(6):
        pick_6.append(random.randint(1, 99))
    return pick_6

def num_matches(winning, ticket):
    num = 0
    match = 0
    while num < 6:
        for i in winning:
            if winning[num] == ticket[num]:
                match += 1
                # print('match')
            # else:
            #     print('None')
            num += 1
    return match

def earnings(m):
    earnings_balance = 0
    if m == 1:
        earnings_balance += 2
    elif m == 2:
        earnings_balance += 7
    elif m == 3:
        earnings_balance += 100
    elif m == 4:
        earnings_balance += 500000
    elif m == 5:
        earnings_balance += 1000000
    elif m == 6:
        earnings_balance += 25000000
    return earnings_balance


def lots_of_plays():
    counter = 0
    balance = 2
    while counter <= 100000:
        balance -= 2
        winning_ticket = pick_6_randos()
        lotto_ticket = pick_6_randos()
        matches = num_matches(winning_ticket, lotto_ticket)
        lotto_winnings = earnings(matches)
        balance += lotto_winnings
        counter += 1
    # return (lotto_winnings - balance) / balance
    return balance




print(lots_of_plays())


#
# matches = num_matches()
# earnings(matches)





# shut up
