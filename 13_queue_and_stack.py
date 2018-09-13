def palindrome(string):
    string = string.lower()

    originStr = []
    reversedStr = []

    for x in string:
        if x.isalpha():
            originStr.append(x)
            reversedStr.append(x)

    while originStr:
        if originStr.pop(0) != reversedStr.pop():
            return False

    return True


def palindrome_without_queuestack(string):
    string = string.lower()

    stringArr = []

    for x in string:
        if x.isalpha():
            stringArr.append(x)

    for i, x in enumerate(stringArr):
        if stringArr[i] != stringArr[-i-1]:
            return False

    return True


print(palindrome("Test string"))
print(palindrome("wow"))
print(palindrome("God's dog"))
print(palindrome("Madam, i'm Adam."))
print(palindrome("Test string"))


print(palindrome_without_queuestack("Test string"))
print(palindrome_without_queuestack("wow"))
print(palindrome_without_queuestack("God's dog"))
print(palindrome_without_queuestack("Madam, i'm Adam."))
print(palindrome_without_queuestack("Test string"))
