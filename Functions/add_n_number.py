def add_n_number(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return add_n_number(n-1)+n
f = add_n_number(9)
print(str(f))

