#
# Paul Ortiz
# 3/2/25
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.

# Get number of bugs collected each day using a for loop.

# Display the total number of bugs collected.

# Program should keep a running total of the number of bugs collected
# The loop should ask for the number of bugs collected each day
#When the loop is finished, the program should display the total number of bugs collected

# Set variable for total (instructional vide says "initalize the accumulator," but my way makes sense to me and this is my code.)
total = 0

# get the bugs collected for each day
for day in range (1, 8) :
    # Print a prompt, instead of the input. The input will actually be the bugs collected per day
    print('Enter the bugs collected on day', day)
    # create a varibale to keep track of bugs
    bugs = int(input())
    # add the number of bugs to the total (accumulator)
    total += bugs
    # keep a running total, but not on the final day otherwise it just shows the total twice. This is cleaner.
    if day < 7 :
        print('Bugs Collected so far: ', total,)

# Display the total bugs
print('You collected a total of', total, 'bugs')

#Ready to test

# Test success, modify to not show running total on final day with "if" statement

# Test Success
# Ready for grading
