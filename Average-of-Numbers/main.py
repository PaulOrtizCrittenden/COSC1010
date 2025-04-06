#
# Paul Ortiz
# 4/5/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#
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

# close the file

myfile.close()

# ready to test
# test success, ready to grade
