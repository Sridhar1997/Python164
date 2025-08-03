# Python Access Specifiers Overview 
# Python uses naming conventions (not keywords) to indicte access control

# Public -> var -> Accessible from anywhere 
# Protected -> _var -> Accessible within class and subclasses (by convention, not enforce)
# Private -> __var -> Name mangled, not accessible outside class directly


# class Student:
#     def __init__(self):
#         self.name="Sridhar"  # Public 
    
#     def show(self):
#         print("Name : ", self.name)

# s=Student()
# s.show()
# print(s.name) 


# class Parent:
#     def __init__(self):
#         self._data="Protected Data"

# class Child(Parent):
#     def display(self):
#         print("Accessing from Child ", self._data)

# c=Child()
# c.display()

class Car:
    def __init__(self):
        self.__engine="V8"
    def show(self):
        print(self.__engine)
        
c=Car()
c.show()
