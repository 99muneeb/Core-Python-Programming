student_grads={"ahmad":34,"ali":49,"hamza":39}
gread=[1,2,33,443,54]
def mean(value):
    if type(value)==dict:
        sum_mean=sum(value.values())/len(value)
    else:
        sum_mean=sum(value)/len(value)
    return sum_mean
print(mean(student_grads))
print(mean(gread))