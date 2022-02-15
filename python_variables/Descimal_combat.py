# Descimal Combat -- Write a function that works with tow integers. whichever the greater number, it subtracts from it the different of the two number plus one. the number that diminishes to 0 first loses. Declare the winner each time.
from numpy import diff


def Combat(num1,num2):
    nums=(num1,num2)
    while(num1*num2>0):
        diff=abs(num1-num2)
        if num1>num2:
            print(num1,'is greater then',num2)
            num1=num1-diff-1
        else:
            print(num1,'is smaller then',num2)
            num2=num2-diff-1
    return nums[1] if num2>num1 else nums[0]
Combat(8,6)
