studentNumbers = [39, 14, 67, 105]
studentNames = ['just', 'john', 'mike', 'summer']


def get_student_number(numbers, names, findName):
    for idx, name in enumerate(names):
        if name == findName:
            return numbers[idx]
    return -1


print(get_student_number(studentNumbers, studentNames, 'just'))
print(get_student_number(studentNumbers, studentNames, 'summer'))
print(get_student_number(studentNumbers, studentNames, 'sd'))
