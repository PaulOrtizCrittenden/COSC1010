#
# Paul Ortiz
# 4/23/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
#
# Let's write a decryption program!
#
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

reverse_dict = {v: k for k, v in swap_dict.items()}

def decrypt(text):
    decrypted = ' '
    for char in text:
        if char in reverse_dict:
            decrypted += reverse_dict[char]
    
    else:
        decrypted += char

    return decrypted

try:
    with open('encrypted.txt', 'r') as infile:
        encrypted_text = infile.read()

    decrypted_text = decrypt(encrypted_text)

except FileNotFoundError:
    print('Error')

print(decrypted_text)
