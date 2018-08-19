import random
import math

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[index] > list[index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1


# 1. Generate random numbers for the numList:
numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

print(numList)
# 2. Initiate the OUTER LOOP
i = len(numList) - 1
while i > 1:
    # 3. Initiate the INNER LOOP
    j = 0
    while j < i:
        # Debbugging
        print("\nIs {} > {}".format(numList[j], numList[j + 1]))
        # 4. User conditional to compare
        if numList[j] > numList[j + 1]:
            print("Switch")
            # 5. Create a temporal Variable to hold the numList[j] value
            temp = numList[j]
            # 6. Assign to the numList[j] value the higest (numLits[j + 1])
            numList[j] = numList[j + 1]
            # 7. Assign the previously stored value of numList[j] to the numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")
        # 8. Increment the INNER LOOP
        j += 1
        for k in numList:
            print(k, end=", ")
        print()
    # 9. Decrement the OUTER LOOP
    print("END OF ROUND")
    i -= 1
# 10. Print the numList values with a for loop
for k in numList:
    print(k, end=", ")
print()
