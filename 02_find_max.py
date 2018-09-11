def find_max(a):
    n = len(a)
    max_v = a[0]

    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]

    return max_v

def findmaxidx(arr):
    pass


v = [17, 33, 66, 88, 34, 22, 6]

print(find_max(v))
