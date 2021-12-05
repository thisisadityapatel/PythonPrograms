#using the class to count the number of objects created form the class

class Fruit():
    count = 0
    def set_data(self, s, c):
        self._size = s
        self._color = c
    
    def __init__(self, s = 0, c = ""):
        self._size = s
        self._color = c
        Fruit.count += 1

    def show_count():
        print(Fruit.count)

def main():
    f1 = Fruit()
    f2 = Fruit()
    f3 = Fruit()
    print()
    print("Counting the number of objects created for the class Fruits : ", Fruit.count)
    print()
    Fruit.show_count()

if __name__ == "__main__":
    main()
    

    
    
        