# file read ---
with open('fist_file.txt','r') as f:
    a=f.read()
print(a)
# file write---
with open('fist_file.txt','w') as f:
    a=f.write('How are you muneeb : ')
print(a)
# file append---
with open('fist_file.txt','a') as f:
    a=f.write('How are you muneeb : ')
print(a)