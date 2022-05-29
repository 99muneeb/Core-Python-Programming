def midal(num1,num2,num3):
    if num1 > num2:
        if num1 < num3:
            middle = num1
        elif num2 > num3:
            middle = num2
        else: 
            middle = num3
    else:
        if num1 > num3:
            middle = num1
        elif num2 < num3:
            middle = num2
        else:
            middle = num3
    print("The middle number is", middle)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter tird number: "))
midal(num1,num2,num3)

