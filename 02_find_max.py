def find_max(a):
    n = len(a)
    max_v = a[0]

    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]

    return max_v


def findmaxidx(a):
    n = len(a)
    # max_v = a[0]
    max_i = 0

    for i in range(1, n):
        if a[i] > a[max_i]:
            max_i = i
    return max_i


def find_min(a):
    n = len(a)
    minValue = a[0]

    for i in range(1, n):
        if a[i] < minValue:
            minValue = a[i]

    return minValue

def find_maxFunc(a):

    return max(a)

v = [17, 33, 66, 88, 34, 22, 6]

print(find_max(v))
print(findmaxidx(v))
print(find_min(v))
print(find_maxFunc(v))
