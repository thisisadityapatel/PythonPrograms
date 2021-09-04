students = {}

number = int(input("Enter the number of student details to be entered : "))

for i in range(number):
    print(f"Student {i+1} : ")
    name = input("Name: ")
    code = input("Code : ")
    print()

    try:
        code = int(code)
    except:
        continue

    #adding the data to the dictionary
    if name not in students:
        students[name] = 0
    students[name] = code

print()
#showing the user the details stored in the dictionary
print(students)
print()


    