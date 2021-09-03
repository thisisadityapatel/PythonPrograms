
def main():
    print("Calculator")
    print("----------")
    print("What function would like to perform?")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Substraction")
    print("4. Division")
    choice = int(input("Enter your choice : "))

    print()
    n1 = int(input("Enter the 1st Number: "))
    n2 = int(input("Enter the 2nd Number: "))

    if choice == 1:
        add(n1, n2)

    if choice == 2:
        multiply(n1, n2)

    if choice == 3:
        sub(n1, n2)

    if choice == 4:
        divide(n1, n2)

def add(x, y):
    print(f"Answer: {x + y} ")

def multiply(x, y):
    print(f"Answer: {x * y} ")

def sub(x, y):
    print(f"Answer: {x - y} ")

def divide(x, y):
    print(f"Answer: {x / y} ")

if __name__ == "__main__":
    main()


