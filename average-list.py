numbers = [1, 1023, 30, 332]

print("Calculating the avg of all the numbers in the list : ", end=" ")

#Method 1(primitive and very logical):
sum = 0
count = len(numbers)

for number in numbers:
    sum = sum + number

print(float(sum/count), end=", ")

print()


