# practice/wall-painting.py

# All our friends are re-painting one wall of their rooms.
# They want us to figure out how much it’s going to cost.
# Assume one gallon of paint covers 400 square feet.
#
# Ask the user for:
#
# Width of the wall
# Height of the wall
# How much a gallon of paint costs
# Figure out then print how much it will cost to paint the wall with one coat.
#
# wall_width = int(input('What is the width of the wall (in feet)? \n'))
# wall_height = int(input('What is the height of the wall (in feet)? \n'))
# paint_cost = int(input('How much does a gallon of paint cost? \n'))
# coats = int(input('How many coats of paint do you plan to put on?\n'))
#
# square_feet = wall_width * wall_height
#
# print('Your wall is ' + str(square_feet) + 'sq ft.')
#
# cost_per_sqft = paint_cost / 400
#
# total_cost = cost_per_sqft * square_feet * coats

# print('It will cost ' + str(total_cost) + ' dollars to paint your wall.')
# ________________________________________________________________________
# ADVANCED VERSION

# def user_inputs():
#     wall_width = int(input('What is the width of the wall (in feet)? \n'))
#     wall_height = int(input('What is the height of the wall (in feet)? \n'))
#     paint_cost = int(input('How much does a gallon of paint cost? \n'))
#     how_many_coats = int(input('How many coats of paint do you plan to put on?\n'))
#     return wall_width, wall_height, paint_cost, how_many_coats
#
# def how_many_sqft(w, h):
#     square_feet = w * h
#     print('Your wall is ' + str(square_feet) + 'sq ft.')
#     return square_feet
#
# def cost_of_wall(cost, sqft, coats):
#     total_cost = cost / 400 * sqft * coats
#     print('It will cost ' + str(total_cost) + ' dollars to paint your wall.')
#
# width, height, cost, coats = user_inputs()
#
# square_footage = how_many_sqft(width, height)
#
# cost_of_wall(cost, square_footage, coats)
#________________________________________________________________________
# SUPER ADVANCED VERSION

def user_inputs():
    wall_width = int(input('What is the width of the wall (in feet)? \n'))
    wall_height = int(input('What is the height of the wall (in feet)? \n'))
    paint_cost = int(input('How much does a gallon of paint cost? \n'))
    how_many_coats = int(input(
    'How many coats of paint do you plan to put on?\n'))
    return wall_width, wall_height, paint_cost, how_many_coats

def how_many_sqft(w, h):
    square_feet = w * h
    print('Your wall is ' + str(square_feet) + 'sq ft.')
    return square_feet

def cost_of_wall(cost, sqft, coats):
    total_cost = cost / 400 * sqft * coats
    if total_cost > cost:
        # math.ciel
    print('It will cost ' + str(total_cost) + ' dollars to paint your wall.')

width, height, cost, coats = user_inputs()

square_footage = how_many_sqft(width, height)

cost_of_wall(cost, square_footage, coats)
