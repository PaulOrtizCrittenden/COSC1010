#
# Paul Ortiz
# Dat4/19/2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#
# Create a list of vowels and initialize an accumulator
#
# main function
def main():
    # get a string from the user
    user_str = input('Enter a string of characters: ')

    # report the vowels and consonants
    print('That string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants')



def num_vowels(s) :
    # make a list containg the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    #intialize the accumulator for vowels
    v_count = 0

    #count the vowels in s
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1
    
    # return the vowel count
    return v_count

def num_consonants(s) :
    #make a list containing vowels again
    vowels = ['a', 'e', 'i', 'o', 'u']

    #initialize the accumulator
    c_count = 0

    # count the consonants in s
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels :
            c_count += 1
    
    # return the consanant count
    return c_count

# ready for testing
# Test Success
# Ready for grading
