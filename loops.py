# while loop
from datastructures import fruits
from datatype import my_college

num=5
while num<15:
    # print(num)
    print(f"loop: {num}")
    if num==10:
        break
    num+=1

# while loop
num1=1
while num1<7:
    num1+=1
    if num==4:
        continue
    print(f"looping: {num1}")

# for loop
fruits = ["banana", "apple", "mango", "orange", "grapes"]

for i in fruits:
    print(i)
my_college="eMobilis M.T.A"

for my in my_college:
    print(my)
