# !important: List all the things that need to happen to solve a problem

# 1. Ask the user to input 2 values and store them in variables num1 and num2
num1, num2 = input('Enter 2 numbres: ').split()
# 2. Convert the strings into regular numbers Integers
num1 = int(num1)
num2 = int(num2)
# 3. Add the values entered and store in sum
sum = num1 + num2
# 4. Substract and store in difference
difference = num1 - num2
# 5. Multiply the values and store in product
product = num1 * num2
# 6. Divide the values and store in quotient
quotient = num1 / num2
# 7. Use modulus on the values to find the remainder
remainder = num1 % num2
# 8. Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))