def game():
    return 90044
score=game()
with open('high_score.txt',) as f:
    high_Score=(f.read()
if high_Score=='':
    with open("high_score.txt", "w") as f:
        f.write(str(score))
elif int(high_Score)<score :
    with open("high_score.txt", "w") as f:
        f.write(str(score))
