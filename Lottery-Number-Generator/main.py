#
# Paul Ortiz
# 4/13/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#
# Create a list with seven elements
#
# we need to import the random module
import random

# set global constants
MAX_DIGITS = 7 # max number of digits
START = 0      # start of the random number range
END = 9        # end of the random number range
#
# Main Function
def main ():
    #create a list
    numbers = [0] * 7
    
    # populate the list
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint(START, END)

    #display the random numbers
    print('Here are your lottery numbers:')
    for index in range(MAX_DIGITS):
        print(numbers[index], end=' ')
    print()

# call the main function
main()

# ready for testing
# Test success
# ready for grading
