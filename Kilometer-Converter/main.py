#
# Paul Ortiz
# 3/9/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Set kilometers as a variable

# set conversion factor
CONVERSION_FACTOR = 0.6214

def main() : 
    # get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles
    show_miles(kilometers)

def show_miles(km) :
    #calculate miles conversion
    miles = km * CONVERSION_FACTOR

    #display the miles
    print(km, 'kilometers equals', miles, 'miles.' )

#call the main function
main ()

# Ready to test
# Test Success
# Ready for Grading
