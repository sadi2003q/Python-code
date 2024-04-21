print("Enter all the grade of the exam : ")
grades = []
while (True):
    number = float(input())
    if number == -1:
        break
    else:
        grades.append(number)

print("The average : ", sum(grades) / len(grades))
print("Maximum grade : ", max(grades))
print("Minimum grade : ", min(grades))