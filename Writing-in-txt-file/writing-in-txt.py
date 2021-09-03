#this program is to write the student details into a .txt file which consists of a name and a student code

number = int(input("Enter the number of student details to be entered : "))

#opening a .txt file to store the student details
file = open("student-details.txt", "w")

for i in range(number):
    print(f"Student {i+1} : ")
    print("-----------------")
    name = input("Name: ")
    code = int(input("Code: "))

    file.writelines(name + ", " + str(code) + "\n")

    print()

print("Student details entered successfully")
file.close()