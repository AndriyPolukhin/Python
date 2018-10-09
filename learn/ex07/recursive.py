# RECURSIVE FUNCTION

# 1. FACTORIAL
# 3! = 3 * 2 * 1


def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


print("4! = ", factorial(4))  # 4! = 24

# 1st: result = 4 * factorial(3) : 4 * 6
# 2nd: result = 3 * factorial(2) : 3 * 2
# 3rd: result = 2 * factorial(1) : 2 * 1


# 2. FIBONACHI NUMBER
# 1, 1, 2, 3, 5, 8, 13

# Fn = Fn-1 + Fn - 2
# Where F0 = 0 and F1 = 1
# print(fib(3))

# 1st: result = fib(2) + fib(1) :  2 + 1
# 2nd: result = (fib(1) = (fib(0)) + fib(0) : 1 + 0

# PROCESS

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result


print(fib(3))
print(fib(4))
print(fib(5))
