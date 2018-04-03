# credit_card.py

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


def check_card_validation():
    card_input = list(input('Enter the cc number:\n'))
    # card_input = '1234567112345679'
    converted_num = []
    for num in card_input:
        converted_num.append(int(num))
    # print(converted_num)
    check_digit = converted_num.pop()
    # print(check_digit)
    # del converted_num[-1]
    # print(converted_num)
    converted_num.reverse()
    # print(converted_num)
    for i in range(len(converted_num)):
        if i % 2 == 0:
            converted_num[i] *= 2
    # print(converted_num)
    sum_list = sum(converted_num)
    # print(sum_list)
    if sum_list % 10 == check_digit:
        print('Valid Credit Card')
    else:
        print('Invalid Credit Card')
    # return converted_num, check_digit










print(check_card_validation())
