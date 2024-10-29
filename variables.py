# variables are containers for storing data values
# variables are created when you assign a value to it
# variables do not need to be declared with any particular type and can even change type after they have been set
# variables are case-sensitive
from itertools import product

# Creating Variables

myname = "Laura"
print(myname)
print("My name is " + myname)
print("My name is " + myname + " and I am learning Python programming.")

print(f"My name is {myname}") # f-string

mynumber = 5
mynumber2 = 7

# print the sum of two variables i
print(mynumber + mynumber2)
print(f"The sum of {mynumber} and {mynumber2} is {mynumber + mynumber2}")
print(f"The product of {mynumber} and {mynumber2} is {mynumber * mynumber2}")
print(f"The quotient of {mynumber} and {mynumber2} is {mynumber / mynumber2}")
print(f"The difference between {mynumber} and {mynumber2} is {mynumber - mynumber2}")

print(type(mynumber))
