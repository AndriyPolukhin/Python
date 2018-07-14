# Enter a string to hide in uppercase : Hide

# Convert to unicode
# Secret Message : 34534633

# Original Message : HIDE

# TIPS:
# 1. Input "Enter a string to hide in uppercase"
# 2. Cycle through each character in the string
# 3. Store each character code in a new string
# 4. Print 'Secret Message : 34537890
# 5. Cycle through each character code 2 at a time by incrememnting by 2 each time
# 6. Get the 1st and 2nd for the 2 digit number
# 7. Convert the code into characters and add them to a new string
# 8. Print Original Mesage: HIDE

# USE : ord("A") | chr(65) for i in range(0, len(str)-1,2) {pr(str[i] + str[i+1])}
# A - Z 65 - 90
# a - z 97 - 122

string = input("Enter a string to hide in uppercase : ")
newStr = "";
orgStr = "";

for char in string:
    i = ord(char) - 23
    newStr += str(i)

for i in range(0, len(newStr)-1, 2):
    toconvert = newStr
    c = chr(int(toconvert[i] + toconvert[i+1]) + 23)
    orgStr += c


print("Original Mesage: {}\n".format(orgStr))
print("Secret Message : {}\n".format(newStr))
print("Original string {} converted to {}\n".format(orgStr, newStr))
