def bubble_sort(data):
    if len(data) < 2:
        return data
    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True
        if not swap:
            break
    return data


print(bubble_sort([9, 22, 1, 55, 2, 8, 5, 44, 100]))
