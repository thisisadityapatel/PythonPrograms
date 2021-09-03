character = input("Enter the desired type of character required : ")
rows = int(input("Enter the number of rows required : "))

# Assigning the space number
space = 30

for i in range(1, rows+1, 1):
    # This loop handles printing the space
    for k in range(space):
        print(" ", end="")

    # This loop handles printing the character
    number = i
    count = -1
    for z in range(number):
        count = count + 2

    for j in range(count):
        print(character, end="")

    print()
    space -=1

print()






