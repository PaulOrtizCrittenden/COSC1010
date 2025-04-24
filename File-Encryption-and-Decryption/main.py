#
# Paul Ortiz
# 4/23/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# 
#


#def char_encrypt():


swap_dict = {'a': '!', 'A': '@',
'b': '#', 'B': '$',
'c': '%', 'C': '^',
'd': '&', 'D': '*',
'e': '(', 'E': ')',
'f': '-', 'F': '_',
'g': '+', 'G': '=',
'h': '{', 'H': '}',
'i': '[', 'I': ']',
'j': ':', 'J': ';',
'k': '"', 'K': "'",
'l': '<', 'L': '>',
'm': ',', 'M': '.',
'n': '?', 'N': '/',
'o': '|', 'O': 'v',
'p': '`', 'P': '~',
'q': '0', 'Q': '1',
'r': '2', 'R': '3',
's': '4', 'S': '5',
't': '6', 'T': '7',
'u': '8', 'U': '9',
'v': 'a', 'V': 'b',
'w': 'c', 'W': 'd',
'x': 'e', 'X': 'f',
'y': 'g', 'Y': 'h',
'z': 'i', 'Z': 'j' , ' ' : ' ' }


    
 
def encrypt(text):
    encrypted = ' '
    for char in text:
        if char in swap_dict:
            encrypted += swap_dict[char]
        
        else:
            encrypted += char
    
    return encrypted

try:
    with open('text.txt', 'r') as infile:
        plain_text = infile.read()

    encrypted_text = encrypt(plain_text)

    with open('encrypted.txt', 'w') as outfile:
        outfile.write(encrypted_text)

    print('Your message has been secured!')

except FileNotFoundError:
    print('Error')
