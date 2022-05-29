def list_number(items):
    max=items[0]
    for x in items:
        if x>max:
            max=x
    return max
print(list_number([1, 2, 33, 45, 765, 6, 7, 9]))