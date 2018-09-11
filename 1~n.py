def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s+i

    return s


def sum_gause(n):
    return n * (n+1) // 2


def sum_sq(n):
    s = 0
    for i in range(1, n+1):
        s = s+i**2

    return s


def sum_sq2(n):
    return n*(n+1)*(2*n+1)//6


print(sum_n(10))
print(sum_n(100))
print(sum_gause(10))
print(sum_gause(100))

print(sum_sq(3))
print(sum_sq(100))
print(sum_sq2(3))
print(sum_sq2(100))
