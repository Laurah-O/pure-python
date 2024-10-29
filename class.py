class fruits:
    # constructor
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"My favourite fruit is {self.name} and it costs {self.price} and it is {self.shape}")

# create instance of a class (object)

myobject=fruits(50,"round","apple")
myobject.display()

