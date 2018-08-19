import random
import math

# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "C"]

randList = ["string", 1.234, 28]

oneToTen = list(range(10))

# print(randList)
# randList = randList + oneToTen
# print(randList)

print(randList[0])

print("list Length : ", len(randList))

first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)

print("Index of string : ", first3.index("string"))

print("How many strings :", first3.count("string"))

first3[0] = " New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

first3.append("Another String")

for i in first3:
    print("{} : {}".format(first3.index(i), i))
