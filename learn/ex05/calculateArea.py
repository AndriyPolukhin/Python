import math


def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "parallelogram":
        parallelogram_area()
    else:
        print("Please enter rectangle or circle")


def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))

    area = length * width

    print("The area of the rectangle is", area)


def circle_area():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    print("The area of a circle is {:.2f}".format(area))


def triangle_area():
    height = float(input("Enter the height : "))
    width = float(input("Enter the width : "))

    area = (height * width) / 2

    print("The area of a triangle is {:.2f}".format(area))


def parallelogram_area():
    length = float(input("Enter the length : "))
    height = float(input("Enter the height : "))

    area = length * height

    print("The area of a parallelogram is", area)


def main():
    shape_type = input("Get area for what shape: ")

    get_area(shape_type)


main()
