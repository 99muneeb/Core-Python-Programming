# Valid_password - write a function that determines wether a string makes for valid password 
# for this it mest be least 6-characters log and most 12 characters long.
# It is also must have a latest one characters  , one digit , and   one characters from $,# and @

def valid_password(password):
    p=list(password)
    if len(password)<6 or len(password)>12:return False
    if not (any(i.ìsdigit()) for i in p):return False
    if not (any(i in '$@#' for i in p)):return False
    if not (any(i.isalpha() for i in p)):return False
    return True
a=valid_password('abc#sfdsf')
print(a)

