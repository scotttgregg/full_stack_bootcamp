# hammer.py

# ask the user what time it is in HH:AM/PM format - save that to a variable
time = input('What time is it? (HH AM/PM)\n')
# use .split() to split the string and assign it to the variable time_split
# .split() returns a list
time_split = time.split(' ')

print(time_split)
# change time_split into an int and assign it to new variable hour -
# given the 0th index
hour = int(time_split[0])
# use .lower() to change input to be lowercase
# assign to new variable and give it 1st index
meridian = time_split[1].lower()


# if hour in range(7, 10) and meridian == 'am', print 'Breakfast time')
# if hour is between 7 and 9
if hour in range(7, 10) and meridian == 'am':
    print('Breakfast time!')
# elif hour in the list [12, 1, 2] and meridian is pm, print lunch time
elif hour in [12, 1, 2] and meridian == 'pm':
    print('Lunch time, bitch!')
# if hour in range(7, 10) or between 7 and 10 not including ten, print
elif hour in range(7, 10) and meridian == 'pm':
    print('Dinner time')
# elif hour in range(10, 12) and meridian = pm, or (hour == 12 or hour )
elif hour in range(10, 12) and meridian == 'pm' or (
    hour in [12, 1, 2, 3, 4, 5] and meridian == 'am'
    ):
    print('Hammer time!')
