# Tale twins :write a function that takes in an integer then checks wether it is greater than the integer that is its mirror image
def Larger_twn(num):
    return num>=int(str(num)[::-1])
a=Larger_twn(923)#(923 and revers digit 329) condiction True
print(a)