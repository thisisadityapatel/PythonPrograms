
#reading the student names and the student code from the student_details.txt file

with open("student-details.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        lst = line.split(",")

        if len(line) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()
        
        print(key + "-" + value)

print()

            
        
