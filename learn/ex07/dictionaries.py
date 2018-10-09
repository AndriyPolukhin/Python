andriyDict = {
    "fName": "Andriy",
    "lName": "Polukhin",
    "address": "16v Street"
}
print("My Name :", andriyDict["fName"])

andriyDict["address"] = "Rosenngraten"
andriyDict["city"] = "Hamburg"
print(andriyDict)

print("Is there a city :", "city" in andriyDict)

print(andriyDict.values())
print(andriyDict.keys())

for k, v in andriyDict.items():
    print(k, v)

print(andriyDict.get("mName", "Not Here"))
print(andriyDict.get("lName", "Not Here"))

del andriyDict["lName"]
print(andriyDict.values())

for i in andriyDict:
    print(i)

andriyDict.clear()

employees = []

fName, lName = input("Enter Employee Name : ").split()

employees.append({'fName': fName, 'lName': lName})

print(employees)
