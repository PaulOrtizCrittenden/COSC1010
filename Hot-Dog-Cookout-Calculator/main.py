#
# Paul Ortiz
# 02/23/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#
# constants

HOT_DOGS_PER_PACKAGE = 10
HOT_DOG_BUNS_PER_PACKAGE = 8

#
# local variables

numAttending = 0 #for the number of people attending
numPerPerson = 0 # the number of hot dogs and buns per person
total = 0        # the total numer of hot dogs and buns needed
minDogs = 0      # the minimum number of packages of hot dogs
minBuns = 0      # the minimum number of pakcages of hot dog buns
dogsLeft = 0     # leftover hot dogs
bunsLeft = 0     # leftover buns

#
# Get the number of people attending the cookout
numAttending = int(input('Enter the number of people attending the cookout; '))

# Get the number of hot dogs per person from the user
numPerPerson = int(input('Enter the number of hot dogs per person; '))

# Calculate the total number of hot dogs and buns needed
total = numAttending * numPerPerson 

# Calculate the minimum number of packs of hot dogs needed
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of hot dogs
if minDogs > 0:
    # calculate the number of hot dogs leftover from a package if any
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    # if there will be leftovers, add an additional package of hot dogs
    if dogsLeft !=0: 
        minDogs += 1

# set the minimum number of packages of hot dogs to one bcause the number of people attending is small enough to require only one package of hot dogs
else: 
    minDogs = 1
    
# Determine the number of leftover hot dogs, if any.
dogsLeft = HOT_DOGS_PER_PACKAGE * minDogs - total

# Calculate the total number of packs of hot dog buns needed
minBuns = total // HOT_DOG_BUNS_PER_PACKAGE

# determine if the number of people attending is large enough to require more than one package of hot dog buns, and then do the rest the same as for hot dogs, but with the buns variables
if minBuns > 0:
    bunsLeft = total % HOT_DOG_BUNS_PER_PACKAGE

    if bunsLeft !=0:
        minBuns +=1
else:
    minBuns = 1

#determine the number of leftover buns, if any
bunsLeft = HOT_DOG_BUNS_PER_PACKAGE * minBuns - total

# Display the minimum packages of hot dogs needed
print('Minimum packages of hot dogs needed: ', minDogs)

# Display the minimum packages of hot dog buns needed
print('Minimum packages of hot dog buns needed: ', minBuns)

# Display the number of hot dogs left over
print('Number of hot dogs left over: ', dogsLeft)

#Display the number of hot dog buns left over
print('Number of hot dog buns leftover: ', bunsLeft)

#Ready to Test
#Test Success
# Ready for grading
