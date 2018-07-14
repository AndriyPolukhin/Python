samp_string = "This is a  very important string"

'''
print(samp_string[0])
print(samp_string[-1])
print(samp_string[3+5])

print("Length:", len(samp_string))
print(samp_string[0:4])
print(samp_string[8:])

print("Green " + "Eggs")
print("Hello " * 5)

num_string = str(4)
print(type(num_string))

# Print the characters:
for char in samp_string:
    print(char)

'''
# Print the characters in paris
for i in range(0, len(samp_string)-1, 2):
    print(ord(samp_string[i]) + ord(samp_string[i+1]))
    print(ord('A'))

# print("65 = ", chr(65))
# A - Z 65 - 90
# a - z 97 - 122