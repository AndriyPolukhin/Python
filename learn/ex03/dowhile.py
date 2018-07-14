# do while loop

# 1. Guess a number between 1 and 10
# 2. Ask again if not true
# 3. If true prints You get the number
# 4. while loop and a break statement



'''
import random
rand_num = random.randrange(1, 10)

i = 1
while (i != rand_num):
   i += 1
prin t("The random values is : ", rand_num)
'''

secret = 7

while True:
    try:
        number = int(input("Guess a number between 1 and 10 : "))
        if (number == secret):
          print("You guessed it")
          break
    except ValueError:
      print("Please enter a number")
    except:
      print("An unknown error")
print("Thank you for playing")