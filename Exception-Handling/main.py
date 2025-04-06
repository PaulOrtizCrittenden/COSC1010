#
# Paul Ortiz
# 4/5/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# 
# to deal with IOErrors, we'll put in a try-except block

try: 
# Open the file

    myfile = open('numbers.txt', 'r')

# We're going to need a total, and then a count of numbers

    total = 0

    count = 0

# read and process

    for line in myfile:
        number = int(line)

# convert lines to integers
        total += number

# get a total count
        count += 1

#calculate and display the average 
    if count > 0:
        average = total / count
        print(int(average)) #first go around I didn't have the average print as an integer, which felt weird because i converted everything else as an integer.
    else:
        print('This file is empty')

# put in exceptions to our try-except block
except IOError as e:
    print('An I/O Erorr Occurred')

# exception for IOError was successful, now let's put in exception for ValueError
except ValueError as e:
    print('A value error has occured')
    
# close the file

myfile.close()

# ready to test
# test success, ready to grade
