def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left, right = [], []
    for i in range(1, len(data)):
        if data[i] < pivot:
            left.append(data[i])
        else:
            right.append(data[i])
    return qsort(left) + [pivot] + qsort(right)


def qsort2(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x < pivot]
    right = [x for x in data[1:] if x >= pivot]
    return qsort(left) + [pivot] + qsort(right)


print(qsort2([4, 11, 678, 22, 1, 8, 12]))
