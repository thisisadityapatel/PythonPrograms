# using the __sub__ and __add__ methods in classes

class Points():
    def __init__(self, intX, intY):
        self.x = intX
        self.y = intY
    
    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        if not isinstance(other, Points):
            raise ValueError("Please Enter instances realted to the class of points.")
        else:
            return Points(self.x + other.x, self.y + self.y)
    
    def __sub__(self, other):
        if not isinstance(other, Points):
            raise ValueError("Please Enter instances realted to the class of points.")
        else:
            return Points(self.x - other.x, self.y - other.y)
p1 = Points(10, 20)
p2 = Points(-4, 14)

print(p1)

print(p1 + p2)

print(p1 - p2)
