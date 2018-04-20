# # change_return.py
#
#
#
dollar_amount = float(input(
    "Input the dollar amount that you have," \
    " so if you have $1.36, enter 1.36.\n"))
total_in_pennies = dollar_amount * 100

amount_of_quarters = total_in_pennies // 25
total_in_pennies = total_in_pennies % 25
amount_of_dimes = total_in_pennies // 10
total_in_pennies = total_in_pennies % 10
amount_of_nickles = total_in_pennies // 5
total_in_pennies = total_in_pennies % 5
amount_of_pennies = total_in_pennies

print("You have " + str(amount_of_quarters) + " quarters.")
print("You have " + str(amount_of_dimes) + " dimes.")
print("You have " + str(amount_of_nickles) + " nickels.")
print("You have " + str(amount_of_pennies) + " pennies.")
