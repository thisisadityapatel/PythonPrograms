import csv

number = int(input("Enter the desired number of student details to be entered : "))

with open("student-details.csv", "a") as file:
    write = csv.writer(file)

    for i in range(number):
        print(f"Student {i+1} : ")
        name = input("Name : ")
        code = int(input("Code : "))

        write.writerow([name, code])
        print("-------------------------------")

print()
print("Details successfully entered into the .csv file")



