from findkey import total

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + key
            if char.islower():  
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  
    return encrypted_text


key = total

original_code = "Sample text" 
encrypted_code = encrypt(original_code, key)
print(encrypted_code)

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 