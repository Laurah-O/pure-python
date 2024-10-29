# create a class called person that has three attributes name, age and gender
# then create a constructor method and method and object

class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old and I am {self.gender}")

myn=person("Laura", "20", "female")
myn.display()