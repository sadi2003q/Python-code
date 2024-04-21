def search(list, target, startingIndex, endingIndex):
    if startingIndex >= endingIndex:
        return False
    mid = (startingIndex + endingIndex) // 2
    if list[mid] == target:
        return True
    elif list[mid] > target:
        return search(list, target, startingIndex, mid)
    elif list[mid] < target:
        return search(list, target, mid+1, endingIndex)


def binary_search(list, n):

    return search(list, n, 0, len(list)-1)


mylist = [519, 1306, 1348, 2920, 3396, 3705, 3920, 4084, 4276,
           4638, 4924, 5630, 6674, 7610, 8231, 8335, 9997, 10168, 11683, 11787]

print(binary_search(mylist, 9997))


