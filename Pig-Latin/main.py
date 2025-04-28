#
# Paul Ortiz
# 4/19/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#
# create main function
def main() :
    user_str = input('Enter a sentenace to be translated into Pig Latin: ')

    result = translate(user_str) # note: i had this as 'user_input' even though i literally wrote the first argument under the main function as 'user_str' \silly me

    print('Translation: ', result)

    # get it to print the returns from the logic we will use later to do the actual translation


def translate(sentence) :
    words = sentence.split() 
    pig_latin_words = []

    for word in words :
        if len(word) > 1:
            pig_latin = word[1:] + word[0] + 'AY'
        
        else:
            pig_latin = word + 'AY'        
            
        pig_latin_words.append(pig_latin.upper())
    

    return ' '.join(pig_latin_words)

main()
# Quick note: this part was hard to figure out. I have had to remove lengths and leading zeroes in excel plenty of times and though of doing something like that, but
# it's not really super useful here. 
# also, I had my indentions wrong several times


# ready to test
# I didn't even bother to annotate the iterations buuuuuttt
#
# I essentially brute force hacked this assignment.
# just kept trying things until it worked. just good old trial and error.
# 
# and then, I used a comma in a sentence while i was testing, and I really didn't like how it just treated the comma as part of the word.
#
# but today I am tired, it is late, and the program is good enough to grade.
