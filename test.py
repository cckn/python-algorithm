import math


def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


def abs_square(a):
    b = a*a
    return math.sqrt(b)

print(abs_sign(5))
print()