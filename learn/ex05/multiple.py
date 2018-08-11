
def mult_divide(num1, num2):
    try:
        return (num1 * num2), (num1 / num2)
    except valueError:
        print("Here we have an error")
    except:
        print("Unknown error")


mult, divide = mult_divide(5, 4)
print("5 * 4 = ", mult)
print("5 / 4 = ", divide)
print("No Error")
