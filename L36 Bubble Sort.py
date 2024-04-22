arr = [1, 5, 7, 98, 4, 2, 12, 55, 36, 88, 77, 99, 12, 2, 31]
def bubble_sort(lst):
    arr = lst
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def bubble_sort2(lst):
    arr = lst
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(bubble_sort(arr))


print(bubble_sort2(arr))