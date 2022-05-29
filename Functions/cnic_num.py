def verified_function(c1):
    list1 = [36401_5534197_5,36401_5534197_6, 36401_5534197_7,36401_5534197_8,36401_5534197_9]
    for i in list1:
        if c1 == i:
            print(f"{i} cnic is  Verified: ")
            break
        else:
            print(f"{i} cnic is Not Verified: ")

c1 = int(input("Enter the cnic Number: "))
verified_function(c1)

