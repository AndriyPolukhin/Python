# !important List all the things that need to happen to solve a problem!

# Problem : Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers

miles = input('Enter amount of miles to convert ')
miles = float(miles)

print("Miles entered: {}".format(miles))

converter = 1.60934

kilometers = miles * converter

print("{} miles equals {:.2f} kilometers".format(miles, kilometers))

kilometers = input('Enter amount of kilometers to convert ')
kilometers = float(kilometers)

miles = kilometers / converter

print("{} kilometers equals {:.2f} miles".format(kilometers, miles))
