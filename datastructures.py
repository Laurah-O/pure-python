# list datastructure, ordered, index

fruits = ["banana", "apple", "mango"]
fruits[1] = "orange"
num=[5,8,1,-3,6,2,0,15]

print(fruits)
print(f"I love eating {fruits[1]}")

for i in fruits:
    print(i)
print(num)

# tuple datastructure, ordered, index, immutable or unchangeable
cars=("toyota", "subaru", "nissan", "mercedes", "audi", "bmw")
print(cars)
print(f"I love {cars[5]} cars")

# set datastructures, unordered, unindexed, no duplicates
colors={"yellow", "red", "blue", "green", "purple", "orange"}
print(colors)

# dictionaries datastructures, mutable(can be changed), key value pairs
staff={"name":"Laura","age":22,"salary":25000}
print(staff)
print(staff["name"])
print(staff["age"])
print(staff["salary"])
