class Fruit():
    count = 0
    def __init__(self, s = 0, c = ''):
        self._size = s
        self._color = c
        Fruit.count += 1
    def show_count():
        print(Fruit.count)

f1 = Fruit()
f2 = Fruit()
Fruit.show_count()
