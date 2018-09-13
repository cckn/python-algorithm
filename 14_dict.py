def findSameName(names):
    nameCount = dict()

    for name in names:
        if name not in nameCount:
            nameCount[name] = 1
        else:
            nameCount[name] = nameCount[name]+1

    return nameCount



print(findSameName(['Tom','jessy', 'Tom','seddle']))