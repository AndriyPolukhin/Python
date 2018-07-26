# Ceaser Cyfer

# A-Z 65-90
# a-z 97-122
# ord(your_letter)
# chr(your_code)

# Check if the character is a letter

# HITS

# 1. Use isupper() to decide which unicodes to work with
# 2. Add the key (number of characters to shift) and if
# the key is bigger or smaller then unicode for
# different letters A, Z, a, z increase or decrease by 26

# 1. Receive the message to encrypt and the number of characters to shift
# 2. Prepare the secret_message
# 3. Cycle through each character in the message
# 4. If it isn't a letter then keep it as it is
# 5. Get the character code and add the shift amount
# 6. If Uppercase then compare to uppercase unicodes
# 7. If bigger then Z substract 26
# 8. If smaller than A add 26
# 9. Do the same for lowercase characters
# 10. Convert from code to letter and add to secret_message
# 11. If not a letter leave character as is
# 12. To decrypt the only thing that changes is the sign of the key
# 13. The same as above

message = input("Enter a mesage to encrypt : ")
key = int(input("Enter number of characters to shift : "))

cyphered = ""

for char in message:
    if not(char.isalpha()):
        cyphered += char
    elif (char.isupper()):
        code = ord(char) + key
        if(code > 90):
            code = code - 26
            code = chr(code)
            cyphered += code
        elif(code < 65):
            code = code + 26
            code = chr(code)
            cyphered += code
        else:
            code = chr(code)
            cyphered += code
    elif (char.islower()):
        code = ord(char) + key
        if(code > 122):
            code = code - 26
            code = chr(code)
            cyphered += code
        elif (code < 97):
            code = code + 26
            code = chr(code)
            cyphered += code
        else:
            code = chr(code)
            cyphered += code
print('The Cyphered :')
print(cyphered)
print('The Decyphered :')
decyphered = ""
for char in cyphered:
    if not(char.isalpha()):
        decyphered += char
    elif (char.isupper()):
        code = ord(char) - key
        if(code > 90):
            code = code - 26
            code = chr(code)
            decyphered += code
        elif(code < 65):
            code = code + 26
            code = chr(code)
            decyphered += code
        else:
            code = chr(code)
            decyphered += code
    elif (char.islower()):
        code = ord(char) - key
        if(code > 122):
            code = code - 26
            code = chr(code)
            decyphered += code
        elif (code < 97):
            code = code + 26
            code = chr(code)
            decyphered += code
        else:
            code = chr(code)
            decyphered += code
print(decyphered)
