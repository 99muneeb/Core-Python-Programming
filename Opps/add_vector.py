class C2dvec:
    def __init__(self,i,j):
        self.iCap=i
        self.jCap=j
    def __str__(self):
        return (f"{self.iCap}i+{self.jCap}j")
class C3dvec(C2dvec):
    def __init__(self,i,j,k):
        super(). __init__(i,j)
        self.kCap=k
    def __str__(self):
        return (f"{self.iCap}i+{self.jCap}j+{self.kCap}k")
vec1=C2dvec(2,3)
vec2=C3dvec(2,3,4)
print(vec1)
print(vec2)
