class employee:
    def get_data(self, n, a, s):
        self._name = n
        self._age = a
        self._salary = s
    
    def show_data(self):
        print(self._name, self._age, self._salary)
    
    def __init__(self, n = '', a = 0, s = 0):
        self._name = n
        self._age = 0
        self._salary = 0
    
    def __del__(self):
        print("Deleting object " + str(self))

e1 = employee()
e2 = employee()
e1.get_data("Aditya", 21, 10000000)
e1.show_data()
e2.show_data()




