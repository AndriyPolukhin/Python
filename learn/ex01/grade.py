# List everything that needs to happen to solve a problem

# Write an age interpreter
# If age is 5 go to Kindergarden
# Age 6 through 17 goes to grades 1 through 12
# if age is greater then 17 say go to college
# if age is different go to work
# Try to complete this programm with 10 lines of code



age = eval(input("Enter your age: "))
if (age >= 0 and age <= 5):
    print("Go to Kindergarden")
elif (age >= 6 and age <=17):
    print("go to ther grade from 1 to 12")
elif (age > 17):
    print("go to college")
else:
    age = eval(input("Enter your age as a positive integer: "))
age
