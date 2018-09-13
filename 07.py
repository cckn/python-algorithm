def find_element(arr, findValue):
    for i, x in enumerate(arr):
        if x == findValue:
            return i

    return -1


def find_all_element(arr, findValue):
    result = []
    for i, x in enumerate(arr):
        if x == findValue:
            result.append(i)

    return result


arr = [33, 44, 22, 44, 55, 33, 1]

print(find_element(arr, 1))
print(find_element(arr, 44))
print(find_element(arr, 33))
print(find_element(arr, 334))


print(find_all_element(arr, 1))
print(find_all_element(arr, 44))
print(find_all_element(arr, 33))
print(find_all_element(arr, 334))
