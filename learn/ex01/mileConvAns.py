# Ask the user to input miles and assign it to the miles variable

miles = input('Enter Miles ')

# Convert to string to integer

miles = int(miles)

# Perform calculation by multiplying 1.6034 times miles

kilometers = miles * 1.6034

# Print results using format()

print("{} miles equalst {} kilometers".format(miles, kilometers))
