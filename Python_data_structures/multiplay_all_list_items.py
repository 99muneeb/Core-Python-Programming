def multiplay_number(items):
    multiplay_all_number=1
    for x in items:
        multiplay_all_number=multiplay_all_number*x
    return multiplay_all_number
print(multiplay_number([2,3,1,5]))