def split_string(s):
    # Splitting the string into a number substring and a letter substring
    num_substring = ''.join([ch for ch in s if ch.isdigit()])
    letter_substring = ''.join([ch for ch in s if ch.isalpha()])
    return num_substring, letter_substring

def convert_to_ascii(substring, is_num=False):
    result = []
    for char in substring:
        if is_num:
            # Convert even numbers to ASCII
            if int(char) % 2 == 0:
                result.append(str(ord(char)))
        else:
            # Convert uppercase letters to ASCII
            if char.isupper():
                result.append(str(ord(char)))
    return result

# Example string
s = "8587enAw3Sk5nnS021125NN784GF"

# Split the string
numbers, letters = split_string(s)

# Convert even numbers and uppercase letters to ASCII
even_number_ascii = convert_to_ascii(numbers, is_num=True)
uppercase_letter_ascii = convert_to_ascii(letters)

# Output the results
print(f"Original String: {s}")
print(f"Even Numbers ASCII: {', '.join(even_number_ascii)}")
print(f"Uppercase Letters ASCII: {', '.join(uppercase_letter_ascii)}")


###Cypher###
def decrypt_caesar(cipher_text, shift):
    decrypted_text = ""
    
    for char in cipher_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Keep spaces and punctuation unchanged
    
    return decrypted_text


# The cryptogram to decrypt
cryptogram = """
VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
"""

# Try all possible shifts from 1 to 25
for s in range(1, 27):
    print(f"Shift Key {s}:")
    print(decrypt_caesar(cryptogram, s))
    print("\n" + "="*50 + "\n")





# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 

