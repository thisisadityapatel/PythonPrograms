#defining the dictionary
students = {}

#opening the txt file to read
with open("student-details.txt", "r") as file:
    
    #reading all the lines in a list names lines
    lines = file.readlines()

    #going over every line
    for line in lines:
        lst = line.split(",")

        #making sure that the line has both the key and value data
        if len(lst) <= 1:
            continue

        #extracting out the key and the value from the list
        key = lst[0].strip()
        value = lst[1].strip()

        #assigning the key and value data into the dictionary
        if key not in students:
            students[key] = 0
        students[key] = value

print()

#showing the data in the dictionary
print("The new dictionary details are : ")
print(students)

