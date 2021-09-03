character = input("Enter the desired type of character required : ")
rows = int(input("Enter the number of rows required : "))

# Assigning the space number
space = 20

for i in range(rows):
    # This loop handles printing the space
    for k in range(space):
        print(" ", end="")

    #This loop handles the printing of character
    for j in range(i):
        print(character, end="")

    space -= 1
    print()

print()

    
