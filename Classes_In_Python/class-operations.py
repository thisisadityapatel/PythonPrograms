#write a class called Number which maintains an integer
class Number:
    def set_number(self, n):
        self._num = n
    def get_number(self):
        return self._num
    def print_number(self):
        print(self._num)
    def isnegative(self):
        if self._num < 0:
            return True
        else:
            return False
    def isdivisible(self, n):
        if self._num % n == 0:
            return True
        else:
            return False
    def absolute_value(self):
        return abs(self._num)

x = Number()
x.set_number(-1234)
x.print_number()

if x.isdivisible(5) == True:
    print("5 divides ", x.get_number())
else:
    print("5 does not divide ", x.get_number())

print("Absolute value of x is :", x.absolute_value())

