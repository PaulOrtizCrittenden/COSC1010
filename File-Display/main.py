#
# Open the file
# For each line in the file:
#   Read the line and display it
# Close the file
#
# step 1: open the file

myFile = open('numbers.txt', 'r')

# read and display the file's contents

for line in myFile:
    number = int(line)
    print(number)

# close the file

myFile.close()

#ready to test
# Test success
#ready to grade
