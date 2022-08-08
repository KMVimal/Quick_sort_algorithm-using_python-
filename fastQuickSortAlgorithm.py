
def quickSort(line):
    length = len(line)
    if length <= 1:
        return line
    else:
        pivot = line.pop()

    itemGreater = []
    itemSmaller = []

    for item in line:
        if item > pivot:
            itemGreater.append(item)
        else:
            itemSmaller.append(item)

    return quickSort(itemSmaller) + [pivot] + quickSort(itemGreater)

print(set(quickSort([5, 4, 2, 8, 3,6,3,7])))
