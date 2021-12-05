class Complex:
    def __init__(self, r = 0.0, i = 0.0):
        self._real = r
        self._imag = i 
    
    def __eq__(self, other):
        if self._real == other._real and self._imag == other._imag:
            return True
        else:
            return False
    
c1 = Complex(1.1, 0.2)
c2 = Complex(2.1, 0.4)
c3 = c1
if c1 == c2:
    print("Same")
else:
    print("Different")

if type(c1) == type(c3):
    print("c1 and c3 are of the same types")
else:
    print("c1 and c2 are of different types")

if c1 is c3:
    print("c1 and c3 are pointing to the same object")
else:
    print("c1 and c3 are pointing to different objects in the class.")