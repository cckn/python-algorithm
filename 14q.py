studentNumbers = [22, 33, 44, 55]
studentNames = ['John', 'Merry', 'Tom', "Jessy"]


d = dict()

for i, x in enumerate(studentNames):
    d[x] = studentNumbers[i]
# print(d)


def getNumber(d, name):
    if name in d:
        return d[name]
    else:
        return '?'


print(getNumber(d, 'Tom'))
print(getNumber(d, 'Tom1'))
