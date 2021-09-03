character = input("Enter the type of character required for bulilding the pyramid : ")
rows = int(input("Enter the number of rows required: "))

for i in range(rows):
    for j in range(0,i,1):
        print(character, end="")
    print()

print()
