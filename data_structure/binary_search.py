import random


def binary_search(data, search):
    if len(data) == 1:
        if search == data[0]:
            return True
        else:
            return False
    if len(data) == 0:
        return False
    medium = len(data) // 2
    if search == data[medium]:
        return True
    elif search > data[medium]:
        return binary_search(data[medium + 1:], search)
    else:
        return binary_search(data[:medium], search)


A = sorted(random.sample(range(50), 10))
print(A)
print(binary_search(A, 19))
print(binary_search(A, 44))
