# Sorting list of instances

class fruits():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def return_price(self):
        return self.price
    
list = [fruits("Mango", 120), fruits("Banana", 20), fruits("Apple", 100)]

for element in sorted(list, key = fruits.return_price):
    print(element.return_price())

