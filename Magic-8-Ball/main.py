#
# Paul Ortiz
# 4/13/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

# open the file to load responses
with open("8_ball_responses.txt", "r") as file:
    responses = [line.strip() for line in file if line.strip()] #this is setting up the responses to interact with randomization

# get program to print a prompt

print('Hello! I am your Magic 8 Ball!')
print('Ask a question! (or type "quit" to exit)')

# begin the loop
while True:
    question = input("\nWhat is your question? ")
    
    if question.lower() == 'quit':
        print('Return for wisdom any time!')
        break
    print('The all-knowing Magic 8 Ball says: ', random.choice(responses))

# ready to test
# test failed because i had a typo in the file name
# take 2
# take 2 failed because of another typ. on a roll here.
# take 3
# take 3 was a success. 
#
# note: don't ask the magic 8 ball questions you don't want an honest answer to.
# ready for grading
