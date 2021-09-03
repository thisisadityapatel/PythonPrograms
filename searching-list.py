student = ["Aditya", "Ayushi", "Elon", "Bill", "Tony"]

name = input("Enter the name of the student : ")

#converting the user entered name into upper case
name = name.upper()

a=0
for i in range(len(student)):
    if student[i].upper() == name:
        print("Student name Present")
        a=1

if a==0:
    print("Student name Absent")


print()