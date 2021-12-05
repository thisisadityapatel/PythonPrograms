#making a class names employee and creating its object

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

    print("Showing the initial constructer set data : ")
    print("Employee 1 : ")
    e1.show_data()
    print()

    print("Employee 2 : ")
    e2.show_data()
    print()

    e1.set_data("Abhinav", 21, 100000)
    e2.set_data("Aaryan", 22, 100000)

    print("Showing the data now set : ")
    print("Employee 1 :")
    e1.show_data()
    print()
    print("Employee 2 :") 
    e2.show_data()

if __name__ == "__main__":
    main()