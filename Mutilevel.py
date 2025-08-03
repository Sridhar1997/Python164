# class GrandParent:
#     def home(self):
#         print("Grandparent's Home")

# class Parent(GrandParent):
#     def car(self):
#         print("Parent's Car")

# class Child(Parent):
#     def bike(self):
#         print("Child's Bike")
    
# c=Child()
# c.home()
# c.car()
# c.bike()


# class A:
#     def __init__(self):
#         print("Class A Constructor")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Class B Constructor")

# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Class C Constructor")

# c=C()



class Company:
    def companyInfo(self):
        print("Credo Systemz")

class Department(Company):
    def deptInfo(Self):
        print("IT")

class Employee(Department):
    def empInfo(self):
        print("Sridhar")
        
e=Employee()
e.companyInfo()
e.deptInfo()
e.empInfo()