def list_number(items):
    min=items[0]
    for x in items:
        if x<min:
            min=x
    return min
print(list_number([1, 2, 33, 45, 765, 6, 7, 9]))