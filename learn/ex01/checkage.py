# We'll provide diferent output based on age
# 1- 18 -> Important
# 21,50, >65 -> Important
# All others -> Not Important

# List
# 1. Receive age and store in age

age = eval(input("Enter age: "))

# and: If Both are true it return true
# or : If either condition is true then it return true
# not : Convert a true condition into a false

# 2. If age is both greater than or equal to 1 and less than or equal to 18 Print Important

if (age >= 1 and age <= 18):
    print("Important Birthday")

# 3. If age is either 21 or 50 Important
elif (age == 21 or age == 50):
    print ("Important Birthday")

# 4. We check if age is less than 65 and then covnert true to false and vice versa
elif not(age < 65):
    print("Not Important Birthday")

# 5. Else Not Important
else:
    print("Sorry Not Important")

