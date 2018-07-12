'''
# Using a random module
import random

# return a random integer between 1 and 50
rand_num = random.randrange(1, 51)

# Working with WHILE LOOPS:
# define the value before the loop starts

i = 1
while (i != rand_num):
    i += 1
print("The random values is : ", rand_num)
'''

y = 1
while y <= 20:
    if (y % 2) == 0:
        y += 1
        continue

    if y == 15:
        break

    print("Odd : ", y)
    y += 1
