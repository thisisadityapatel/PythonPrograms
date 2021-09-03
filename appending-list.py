studentnames = []

number = int(input("Enter number of student names to be entered :  "))

for i in range(number):
    student_name = input(f"Name {i+1} : ")
    studentnames.append(student_name)

#showing all the names in the list
print()
print("The details in the list are: ")
for name in studentnames:
    print(name)

print()