# 3>=3
# True

# a=7
# a**=3
# print(a)

# 7>7 and 2>-1
# false

# a=2^2
# print(a)

# Next prefect square -- A prefect square  is an integer , the square root of which is also an
# integer . write a fuction that takes in  non-negative integer and return the next prefect square
# If interger ,however , is not a prefect square itself , it makes it known.

import math


def next_prefect_square(num):
    return int(math.sqrt(num)+1)**2 if math.sqrt(num) % 1 == 0 else "Not a prefect square itslef "


a = next_prefect_square(49)
print(a)
