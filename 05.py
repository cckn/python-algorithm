def gcd(a, b):
    minNumber = min(a, b)

    for n in range(minNumber, 0, -1):
        if (a % n == 0) & (b % n == 0):
            return n


def gcd_recursive(a, b):
    minValue = min(a, b)
    maxValue = max(a, b)
    if minValue == 0:
        return maxValue

    return gcd_recursive(minValue, maxValue % minValue)


print(gcd(6, 4))
print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))


print(gcd_recursive(6, 4))
print(gcd_recursive(1, 5))
print(gcd_recursive(3, 6))
print(gcd_recursive(60, 24))
print(gcd_recursive(81, 27))
