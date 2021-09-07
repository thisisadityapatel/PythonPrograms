import csv
a=0
with open("student-details.csv", "r") as file:
    name = input("Enter the name of the student whose details are to be searched: ")

    read = csv.reader(file)

    for row in read:
        if name in row:
            print("Name Found !!")
            print("Details: ")
            print("-------")
            print(row)
            a = 1

if a == 0:
    print("Name not found!!")

        
        