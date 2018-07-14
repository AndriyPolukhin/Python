# Use fro loop throught the list from 1 to 21
# Use modulus to check that the result is NOT EQUAL to 0
# Print the odds


print("The range 1,21 loop")
for i in range(1,21):
    if i % 2 != 0:
		    print(i)
		    continue

print("The range 5 loop")

for x in range(5):
    print(x)

print("The range from 3 to 6 loop")
for x in range(3,6):
    print(x)

print("The range of each 2 from 3 to 8")
for x in range(3, 8, 2):
    print(x)


print("While Loop")
count = 0
while count < 5:
    print(count)
    count = count + 1


print("With break and continue")

count = 0
while True:
    print(count)
    count = count + 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("With else clause")

count = 0
while(count<5):
    print(count)
    count = count + 1
else:
    print("count value ereached %d" %(count))


print("for with Else")
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")



