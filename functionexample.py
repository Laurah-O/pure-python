def emobirubyclass(name,age,gender):
    print(f"student name is :{name} age: {age} gender: {gender}")
emobirubyclass("laura",23, "female")
emobirubyclass("rdynaset", "21", "male")

name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
gender = input("Enter the student's gender: ")

emobirubyclass(name, age,gender)


def calculate_area(length, width):
    area = length * width
    print(f"The area of the rectangle is: {area} square units")

# Get user input for the parameters
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Call the function with the input values
calculate_area(length, width)