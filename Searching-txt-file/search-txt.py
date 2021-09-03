#searhing the student-details.txt with the name the student entered
with open("student-details.txt", "r") as file:
    lines = file.readlines()
    name = input("Enter the name of the student whose details are to be searched : ")
    name = name.upper()
    a = 0
    for line in lines:
        lst = line.split(",")

        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        key = key.upper()

        if key == name:
            print("Name Found")
            a = 1

    if a == 0:
        print("No Name found")

print()
    