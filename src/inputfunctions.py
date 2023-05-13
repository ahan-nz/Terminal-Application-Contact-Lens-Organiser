import sys

# Function for if input isn't 'y' or 'n' when asked
def y_or_n():
    print('Please enter \'Y\' or \'N\'.')

# Function for when the number of invalid inputs exceeds the for loop
def invalid_choices():
    print('Too many invalid choices, programme ending.')
    sys.exit(1)