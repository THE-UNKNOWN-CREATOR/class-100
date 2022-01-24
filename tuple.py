maxmin = (9, 7, 8, 3, 1, 5, 2, 6, 4)

def bigsmallnumber(numbers):
    biggest = 0
    smallest = 100
    for n in range(9):
        if numbers[n] > biggest:
            biggest = numbers[n]
        if numbers[n] < smallest:
            smallest = numbers[n]
    return biggest, smallest

print(bigsmallnumber(maxmin))
