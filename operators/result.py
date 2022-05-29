subject_1=int(input("Ënter the first subject marks: "))
subject_2=int(input("Ënter the second subject marks: "))
subject_3=int(input("Ënter the third subject marks: "))
total=subject_1+subject_2+subject_3

if subject_1<33 or subject_2<33 or subject_3<33:
    print("You are fail  :(")
elif total/3<40:
    print("You are fail because your marek is less then 40%:")
else:
    print("You are pass congraulaction!")

