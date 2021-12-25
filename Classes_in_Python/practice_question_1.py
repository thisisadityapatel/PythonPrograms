class number():
    def set_number(self, n):
        self._number = n
    
    def get_number(self):
        return self._number
    
    def print_number(self):
        print(self._number)
    
    def isnegative(self):
        if self._number < 0:
            return True
        else:
            return False
    
    def isdivisible(self, n):
        if self._number % n == 0:
            return True
        else:
            return False

    def absolute_value(self):
        if self._number < 0:
            return (-self._number)
        else:
            return self._number

def main():
    x = number()
    x.set_number(-1234)

    if x.isdivisible(5) == True:
        print("5 divides ", x.get_number())
    else:
        print("5 does not divide ", x.get_number())

    print("Abs value is : ", x.absolute_value())



if __name__ == "__main__":
    main() 
