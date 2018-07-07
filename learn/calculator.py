# List everything that need to happen to solve a problem

# Create a calcualtor that performs operations
# Enter Calculation: 5 * 6
# Print 5 * 6 = 30

# THE LIST:

## 1. Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation: ').split()

## 2. Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

## 3. If + then we need to provide output based on addition
if operator == "+":
  print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
  print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
  print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
  print("{} / {} = {}".format(num1, num2, num1/num2))
else:
	print("Use either +, -, *, / next time")

## 4. Print the result
