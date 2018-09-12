def find_element(arr, findValue):
    for i, x in enumerate(arr):
        if x == findValue:
            return i

    return -1


arr = [33, 44, 22, 44, 55, 33, 1]

print(find_element(arr, 1))

print(find_element(arr, 44))

print(find_element(arr, 33))
print(find_element(arr, 334))
