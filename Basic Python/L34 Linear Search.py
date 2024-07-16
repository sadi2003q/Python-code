def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i += 1
    return False



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if search(my_list, 7):
    print("Found")
else:
    print("Not found")
