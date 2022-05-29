class Student:
    institute="pny"
    def __init__(self,name,cnicNo,phonNo,institute):
        self.name=name
        self.cnicNo=cnicNo
        self.phonNo=phonNo
        self.institute=institute
    def getdata(self):
        print(f"Name is {self.name} phone no is {self.phonNo} cnic No is {self.cnicNo} and institute {self.institute}")
muneeb=Student("Muneeb",3042630299,3640155341975,"pny")
muneeb.getdata()
