# Cypher:
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

message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26) : "))

secret_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char

print("Encrypted :", secret_message)

key = -key
orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        orig_message += chr(char_code)
    else:
        orig_message += char

print("Decrypted :", orig_message)
