f = open("test.txt", "r")
print(f.read())  # reading file

# print(f.readline())  # read only one line

f = open("test.txt", "a+")

f.write("writing file with appending")

print(f.read())


# opening file with binary format (for image video)
# use 'rb'