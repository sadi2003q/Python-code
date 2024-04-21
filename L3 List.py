nums = [1, 2, 3, 4, 5, 6, 7, 8]

print(nums[0])
print(nums[-2])
print(nums[2:4])

names = ['John', 'Smith', 'adnan']
print(names)

values = [9.6, 'sadi', 25]

multipleList = [[1, 2, 3], ['adnan', 'abdullah', 'sadi']]

nums.append(23)  # insert at the last
nums.insert(2, 42)

nums.remove(4)
nums.pop(2)  # based on index
del nums[2: 4]

nums.extend([44, 55, 66])
print(min(nums))
print(max(nums))
print(sum(nums))
print(nums.sort())
