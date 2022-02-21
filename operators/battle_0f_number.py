# Write a function that takes a list and return that greater then without using max() function
def Battle_of_numbers(numbers):
    winner=numbers[0]
    for num in numbers:
        if num>winner :winner=num
        # return winner (for smalllist number)
    return winner
a=Battle_of_numbers([4,5,6,7,8,32])
print(a)