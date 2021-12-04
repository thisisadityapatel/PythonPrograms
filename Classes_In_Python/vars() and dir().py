#vars() and dir() in classes

class fruits:
    count = 0

    def __init__(self, name = "", size = 0, color = ""):
        self._name = name
        self._size = size
        self._color = color
        fruits.count += 1
    
    def display():
        print(fruits.count)

f1 = fruits("Banana", 5, "Yellow")
print(vars(fruits))
print(dir(fruits))
print(vars(f1))
print(dir(f1))

