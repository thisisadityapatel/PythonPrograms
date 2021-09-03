classdetails = ["Aditya", "Ayushi", "Elon", "Bill", "Steve"]

delete = input("Enter the name of the sstudent whopse details are to be deleted: ")

if delete not in classdetails:
    print("Invalid student name")

classdetails.remove(delete)

#displaying the new class details
print(classdetails)
