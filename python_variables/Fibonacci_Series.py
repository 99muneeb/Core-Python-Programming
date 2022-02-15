
# Fibonacci Series - write a function that takes , from the user , the number to prnt and prnts the fibonacci series upto the length.
def fib(length):
    a,b,count=0,1,0
    while (count<length):
        print(a,end=', ')
        count +=1
        a,b=b,a+b
    print('...........')
# fib(5)
fib(3)
