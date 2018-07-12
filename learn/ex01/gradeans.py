# Ask fro the age

age = eval(input("Enter age: "))

# Handle if age < 5

if age < 5:
    print("Too young for school")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarden")

# Since a number is the result for age 6 - 17 we can check them all with 1 condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))

# Handle everyone else
else:
    print("Go to College")
