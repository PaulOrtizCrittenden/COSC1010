#
# Paul Ortiz
# 4/23/2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

#constant for the number of states to quiz the user on
NUM_STATES = 50

def main():
    #initialize the state_caps dictionary
    state_caps = state_cap_dictionary()

    #intial varibales to keep count of the answers
    correct = 0
    incorrect = 0

    #quiz the user
    for count in range(NUM_STATES):
        #get a random entry from the dictionary.
        state, capital = state_caps.popitem()

        #quiz the user
        print('What is the capital of ', state, '? ', end=' ')
        response = input()

        # is the answer correct?
        if response.lower() == capital.lower():
            correct += 1
            print('Correct!')
        
        else:
            incorrect += 1
            print('Incorrect.')
    
    # Display the results
    print('Correct responses: ', correct)
    print('Incorrect repsonses: ', incorrect)

    # Initialize dictionary
    
def state_cap_dictionary():
    
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    return capitals

    # Local variables

 
    # Continue until user quits the game.

# Call the main function.
main()
