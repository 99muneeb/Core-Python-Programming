import random
def gamewin(computer,you):
    if computer==you:
        return None
    elif computer=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif computer=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif computer=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("Computer Turn:snake(s) water(w) or gen(g)? ")
randomNO=random.randint(1,3)
if randomNO==1:
    computer='s'
elif randomNO==2:
    computer='w'
elif randomNO==3:
    computer='g'
you=input("Computer Turn:snake(s) water(w) or gen(g)? ")
a=gamewin(computer,you)
print(f"computer chose:{computer} ")
print(f"you chose:{you} ")
if a==None:
    print("Game is tie: ")
elif a:
    print("you Win: ")
else:
    print("YOur lose: ")

