import random
import math

# 1. Create a list of 5 numbres
# 2. Using a for loop go throug the range of 1 - 9
# 3. Printh the values

# My Answer
listOfFive = []

for i in range(10):
    if(i % 2 == 0):
        listOfFive.append(i)

print(listOfFive)

# Dereks solution

numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

for i in numList:
    print(i)

# For random Dereks is the actual thing
