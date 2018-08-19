import random
import math

"""
# I. Generate a MultiPlication table
Expected Answer:
1, 2, 3, 4, 5, 6, 7, 8, 9
2, 4, 6, 8, 10, 12, 14, 16, 18,
...
9, 18, 27, 36, 45, 54, 63, 72, 81
"""

# 1. Cerate a multidimensional list
multTable = [[0] * 10 for i in range(10)]
# 2. Increment with outer for
for i in range(1, 10):
    # 3. Increment with inner for
    for j in range(1, 10):
        # 4. Assign the value to the call
        multTable[i][j] = i * j
# 5. Output the data
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=", ")
    print()
