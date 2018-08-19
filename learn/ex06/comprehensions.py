import random
import math

# 1. Generate a Event List
# evenList = [i*2 for i in range(10)]
# for i in evenList:
#     print(i)

# 2. Power of 2,3,4
numList = [1, 2, 3, 4, 5]
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]
for i in listOfValues:
    print(i)
print()

# 3. Generate a multiDimensional List
# multDList = [[0] * 10 for i in range(10)]
# multDList[0][1] = 10
# print(multDList[0][1])
# print(multDList)
