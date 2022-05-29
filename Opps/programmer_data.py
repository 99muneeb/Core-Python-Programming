class Programms:
    Company = "Mecrosoft"
    def SetData(self, name, phone,Company):
        self.name = name
        self.phone = phone
        self.Company = Company
    def getData(self):
        print(f"Compnay is :{self.Company}")
        print(f"Name is :{self.name}")
        print(f"phone NO is :{self.phone}")
a = Programms()
a.SetData("Muneeb",304630299,"Mecrosoft")
a.getData()

