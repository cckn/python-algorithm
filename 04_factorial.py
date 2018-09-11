def factorial(n):
    result = 1
    for num in range(1, n+1):
        # print(num)
        result = result * num
    return result


def factorial2(n):
    if n == 1:
        return 1
    return n * factorial2(n-1)


print(factorial(3))
print(factorial(5))
print(factorial(10))


print(factorial2(3))
print(factorial2(5))
print(factorial2(10))