letter_z = "z"
num_3 = "3.14"
a_space = " "

# Check for type
'''
print("Is z a letter or number :", letter_z.isalnum())
print("Is z a letter :", letter_z.isalpha())
print("Is 3 a number :", num_3.isdigit())
print("Is z a lowercase :", letter_z.islower())
print("Is z a uppercase :", letter_z.isupper())
print("is space is space :", a_space.isspace())
'''

# Functions


def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


print("Is Pi a Float :", isfloat(num_3))
