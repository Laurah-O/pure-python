# Create a program that checks a student performance
marks=int(input("Enter your marks: "))

if 100 >= marks >= 80:  #if marks<=100 and marks>=80:
    print("You have an A")
elif 79 >= marks >= 60:
    print("You have a B")
elif 59 >= marks >= 40:
    print("You have a C")
elif 39 >= marks >= 0:
    print("You have Failed")
else:
    print("Invalid marks")

# Create a program that is going to calculate bmi

# def bmi():
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))
#
#     bmi = weight / (height ** 2)
#
#     if bmi < 18.5:
#         print(f"Your BMI is {round(bmi, 2)} and you are underweight")
#     elif 18.5 <= bmi < 24.9:
#         print(f"Your BMI is {round(bmi, 2)} and you have normal weight")
#     elif 25 <= bmi < 29.9:
#         print(f"Your BMI is {round(bmi, 2)} and you are overweight")
#     else:
#         print(f"Your BMI is {round(bmi, 2)} and you are obese")

# Get user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Display the result
print(f"\nYour BMI is: {round(bmi, 2)}")
print(f"Category: {category}")