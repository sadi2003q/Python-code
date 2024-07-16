from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



evenList = list(filter(lambda num: num % 2 == 0, nums))
oddList = list(filter(lambda num: num % 2 == 1, nums))

doubleEvenValue = list(map(lambda num: num * 2, evenList))
print(doubleEvenValue)



summation = reduce(lambda x, y: x+y, oddList)
print(summation)