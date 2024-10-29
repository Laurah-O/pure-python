# python script that checks if a number is even or odd number

num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Create a program that prints the largest of the three numbers

num2=int(input("Enter first number: "))
num3=int(input("Enter second number: "))
num4=int(input("Enter third number: "))

if num2>num3 and num2>num4:
    print(f"{num2} is the largest number")
elif num3>num2 and num3>num4:
    print(f"{num3} is the largest number")
else:
    print(f"{num4} is the largest number")

# Python script to simulate a traffic light

light = input("Enter the traffic light color (red, yellow, green): ").strip().lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready")
elif light == "green":
    print("Go")
else:
    print("Invalid color")