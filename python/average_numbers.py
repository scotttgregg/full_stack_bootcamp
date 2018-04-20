# average_number.py






nums = []


while True:
    user_input = input('Enter a number, or "done": ')
    if user_input != 'done':
        number = int(user_input)
        nums.append(number)
    elif user_input == 'done':
        for i in range(len(nums)):
            total = sum(nums)
            average = total / len(nums)
        print(average)
        break
    else:
        print("not a valid option")
