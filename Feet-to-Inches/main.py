#
# Paul Ortiz
# Dat3/9/2025
# Feet to Inches Programming Project
# COSC 1010
#
# constant for the number of inches per foot, we're using it as a conversion factor
INCHES_PER_FOOT = 12

# main function
def main() : 
    #get a number of feet from the user
    feet = int(input('Enter a number of feet: '))

    # Co9nvert that to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

# The feet_to inches function converts feet to inches
def feet_to_inches(feet) : 
    return feet * INCHES_PER_FOOT

# Call the main function
main()

# Ready to test
# Test Success
#
# Ready for Grading
