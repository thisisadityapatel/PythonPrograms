students = {
    "Aditya": 211202,
    "Tony": 112233,
    "Elon": 69420,
}

name = input("Enter the name that you want to search in the dictionary : ")

if name in students:
    print("Name Present")
    print(f"{name} , {students[name]}")

else:
    print("Name Absent")
    
