# CREATE A CUSTOMER LIST
# THE OUTPUT OF THE PROGRAMM SHOULD BE
# OUTPUT:
# Enter Customer (Yes/No): y
# Enter Customer Name: Andriy Polukhin
# Enter Customer (Yes/No): y
# Enter Customer Name: Anasatsia Tsukrova
# Enter Customer (Yes/No): n
# Andriy Polukhin
# Anastasia Tsukrova

# PROCESS
# 1. Create an array
# 2. Create a loop
# 3. Enter y or n/ Get input and make it work for y or n
# 4. Check to leave loop
# 5. Get customer data
# 6. Add customer data to list
# 7. Print customer data

# Solution
customers = []
while True:
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()
    if createEntry == 'n':
        break

    else:
        fName, lName = input("Enter Customer Name : ").split()
        customers.append({'fName': fName, 'lName': lName})

for cust in customers:
    print(cust['fName'], cust['lName'])
