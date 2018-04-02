# grade conversion

grade_percentage = int(input('What is your grade score (0 - 100): '))

if grade_percentage >= 97:
    print('You have an A+')
elif grade_percentage >= 93:
    print('You have an A')
elif grade_percentage >= 90:
    print('You have an A-')
elif grade_percentage >= 87:
    print('You have a B+')
elif grade_percentage >= 83:
    print('You have a B')
elif grade_percentage >= 80:
    print('You have a B-')
elif grade_percentage >= 77:
    print('You have a C+')
elif grade_percentage >= 73:
    print('You have a C')
elif grade_percentage >= 70:
    print('You have a C-')
elif grade_percentage >= 67:
    print('You have a D+')
elif grade_percentage >= 63:
    print('You have a D')
elif grade_percentage >= 60:
    print('You have a D-')
else:
    print('You are a failure.')
