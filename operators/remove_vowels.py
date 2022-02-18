# Remove vowels - werit a function that take a string and remove any vowels in it.
def remove_vowels(string):
    s=''
    for letter in string:
        if letter not in ['a','e','i','o','u']: s+=letter;
    return s
a=remove_vowels("Hellow Muneeb")
print(a)


