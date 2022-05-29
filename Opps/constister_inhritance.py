class Student1:
    def __init__(self):
        # self.consister="Bace class"
        print("consister called by base calss")
class Student2(Student1):
    def __init__(self):
        # self.consister="Derived class"
        print("consister called by derived class")
# B=Student1()

D=Student2()
