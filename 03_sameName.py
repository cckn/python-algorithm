def findSameName(arr):
    exist = set()
    sameName = set()

    for name in arr:
        if name in exist:
            sameName.add(name)

        else:
            exist.add(name)

    return sameName


arr = ["tom", "tom", "Yudi", "crh","tom"]
print(findSameName(arr))
