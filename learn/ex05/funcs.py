'''
def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 =", add_numbers(5, 4))

def assign_name():
    name = "Doug"

assign_name()
print(name)


glb_name = "Sally"
print(glb_name)


def change_name():
    global glb_name
    glb_name = "Sammy"


change_name()
print(glb_name)
'''


def get_sum(num1, num2):
    sum = num1 + num2


print(get_sum(5, 4))
