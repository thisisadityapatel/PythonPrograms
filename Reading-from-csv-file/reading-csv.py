import csv
students = []

file = open("student-details.csv", "r")

read = csv.reader(file)

for row  in read:
    for col in row:
        print(col, end=", ")
    print()
file.close()
