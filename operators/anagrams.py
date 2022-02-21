
# Anagrams: write a function taken two  string and check the weather the Anagrams,reranging letter and other letter

def Anagram(w1,w2):
    return sorted(w1.lower())==sorted(w2.lower())
a=Anagram('alter','alter')
print(a)