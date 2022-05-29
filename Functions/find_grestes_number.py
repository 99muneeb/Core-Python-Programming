num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
num3=int(input("Enter the num3: "))

def gratest(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
m=gratest(num1,num2,num3)
print("The masximun number is : ",str(m))
