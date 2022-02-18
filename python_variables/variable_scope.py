
# program(1)
# def counter():
#     global a
#     a=2
#     print(a)
# counter()


# program(2)
# def red():
#     a= 1
#     def blue():
#         a=2
#         b=2
#         print(a)
#         print(b)
#     blue()
#     print(a)
# red()


# program(3)
def red():
    a= 1
    def blue():
        nonlocal a
        a=2
        b=2
        print(a)
        print(b)
    blue()
    print(a)
red()
