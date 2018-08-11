# Solve for X:
# x + 4 = 9
# X will always be the 1st value received and you only
# will deal with addition
# 1. Recieve the string and split the string into variables
# 2. Convert the string into ints (just the numbers)
# 3. Convert the result into a string and join or concatenate it to the string "X = "
# 4. print()
'''
x, operator, y, operator2, ans = input("Enter the expression : ").split()
# x = int(x)
y = int(y)
ans = int(ans)
expression = ""
def get_ans(x, y, ans):
    x = -y + ans
    return x
x = get_ans(x, y, ans)
print(x)
'''

# X will always be the 1st value received and you only
# will deal with addition

# 1. Recieve the string and split the string into variables


def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

# 2. Convert the string into ints (just the numbers)
    num1, num2 = int(num1), int(num2)

# 3. Convert the result into a string and join or concatenate it to the string "X = "
    return "x = " + str(num2 - num1)

# 4. print()


print(solve_eq("x + 4 = 9"))


def solve_equation(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)


print(solve_equation("x + 5 = 11"))
