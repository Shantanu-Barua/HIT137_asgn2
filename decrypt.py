from findkey import total
import pandas as pd

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) - key  # Shift backwards
            if char.islower():  
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():  
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  
    return decrypted_text

print('The Key: ', total, '\n')
key = total 

print('Encrypted code: \n')
# Open the encrypted code
with open('encrypted_code.txt', 'r') as file:
    encrypted_code = file.read()

# Decrypt the encrypted code
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)

with open('final_decrypted_code.txt', 'w') as file:
    file.write(decrypted_code)


# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 
