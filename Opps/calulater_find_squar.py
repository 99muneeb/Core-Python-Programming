class Calulater:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"The value of {self.num} square is {self.num **2}")
    def squar_root(self):
        print(f"squa root no {self.num}  is :{self.num**0.5}")
    def quab(self):
        print(f"squa root no {self.num}  is :{self.num**3}")
a = Calulater(3)
a.square()
a.squar_root()
a.quab()

