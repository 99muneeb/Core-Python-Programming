def Max(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        print("num1 is smallast number: ")
    elif num2 < num1 and num2 < num3:
        print("num2 is smallast number:")
    else:
        print("num3 is smallast number: ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
Max(num1,num2,num3)
