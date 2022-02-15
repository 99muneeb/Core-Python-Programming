# Integers come in the all ssize -- write a function that takes in an integer and gets its length without using the len() function
def size(n):
    count=0
    while (n>1):
        count +=1
        n/=10
    return count;
count_no=size(101)
print(count_no)
