# Have a user enter their investemnt amount and expected interest per yaer
# Each year their investment wil increase by their investment + their investment * interest rate is
# Print out tje earning after a 10 year period


# TIPS:
# 1. Ask for the money invested + the interest rate
# 2. Convert the value to a float
# 3. Convert the value to a float and round the precentage rate by 2 digits
# 4. Cycle through 10 years using a for loop and range from 0 to 9
# 5. Output the results


money = input("How much to invest: ")

interest_rate = input("Interest Rate: ")

money = float(money)

interest_rate = float(interest_rate) * .01

for y in range(0,9):
    money = money + (money * interest_rate)


print("Investment after 10 years : {:.2f}".format(money))
