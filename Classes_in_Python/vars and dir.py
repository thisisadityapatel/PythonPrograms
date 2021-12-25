#using vars() and dic in classes of the python

class employee():
    def set_data(self, n, a, s):
        self._name = n
        self._age = a
        self._salary = s
    
    #making the constructor for the class
    def __init__(self, n = "", a = 0, s = 0):
        self._name = n
        self._age = a
        self._salary = s
    
    def show_data(self):
        print(f"Name : {self._name}")
        print(f"Age : {self._age}")
        print(f"Salary : {self._salary}")

def main():
    e1 = employee()
    e2 = employee()
    e1.set_data("Abhinav", 21, 100000)
    e2.set_data("Aaryan", 22, 100000)
    print()
    print(vars(employee))
    print()
    print(dir(employee))
    print()
    print(vars(e1))
    print()
    print(vars(e2))
 

if __name__ == "__main__":
    main()