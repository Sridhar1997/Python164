# Create a Class - Create Object

# class display:
#     name="Sridhar"
#     age=27
    
# p1=display()
# print(p1.name)
# print(p1.age)

# __init__() Method- automatically every time the class is being used to create a new object

# class display:
#     def __init__(self, name, age):
#         self.name=name 
#         self.age=age 

# p1=display("Sridhar", 27)

# print(p1.name)
# print(p1.age)


# __str__() - method controls what should be returned when the class object is represented as a string 
# method is not set, the string representation of the obejvt is returned

# class display:
#     def __init__(self, name, age, role):
#         self.name=name 
#         self.age=age 
#         self.role=role 
    
#     def __str__(self):
#         return f"Name - {self.name} Age - {self.age} Role - {self.role}"

# p1=display("Sridhar Raj P",27, "Trainer")
# print(p1)


#  Create Methods (Functions)

# class display:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age 
        
#     def myfunction(self):
#         print("Name "+self.name +" Age - "+self.age)
    
# p1=display("Sasi", "24")
# p1.myfunction()




# class display:
#     def __init__(self, name, age):
#         self.name=name 
#         self.age=age 
    
#     def myfunction(self):
#         print(self.name)
#         print(self.age)

# p1=display("Abi", 27)
# p1.myfunction()

# p1.name="Abi A"
# p1.age=28 

# p1.myfunction()

# # del p1.age 

# # print(p1.age)

# del p1 

# print(p1)




# Basic Class and Object

# class Person:
#     def greet(self):
#         print("Welcome to Credo Systemz")

# p=Person()
# p.greet()

# Class with Constructor 

# class Student:
#     def __init__(self, name):
#         self.name=name 
    
#     def show(self):
#         print("Student Name: ", self.name)
    
# s=Student("Sridhar Raj P")
# s.show()  





# Class with Two Attributes 

# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length 
#         self.width=width 
    
#     def area(self):
#         return self.length * self.width 

# r=Rectangle(5, 3)
# print("Area : ", r.area())


# Class with Method Returning Value 

# class Circle:
#     def __init__(self, radius):
#         self.radius=radius 
    
#     def circumference(self):
#         return 2*3.14*self.radius 

# c=Circle(7)
# print(c.circumference())


# Class with Default Constructor 

# class Car:
#     def __init__(self):
#         self.brand="BMW"
#     def show(self):
#         print(self.brand)

# c=Car()
# c.show()


# What is Inheritance? -Inheritance is an OOP Concept Where a class (called the child or subclass) inherits 
# the properties and methods of antoher class (called the parent or superclass)

# Single - One Child Inherits from One Parent
# Multilevel - Child Inherits from a Parent, which inherits from another Parent 
# Multiple - Child Inherits from multiple parents 
# Hierarchical - Multiple Children  inherit from the same parent
# Hybrid - Combination of more than one type of inheritance 



# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")


# d=Dog()
# d.sound()
# d.bark()



# class Animal:
#     def eat(self):
#         print("Eating")

# class Mammal(Animal):
#     def walk(self):
#         print("Waling")

# class Dog(Mammal):
#     def bark(self):
#         print("Barking")

# d=Dog()
# d.eat()
# d.walk()
# d.bark()



class Father:
    def skills(self):
        print("Gardening")
    
class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def ownskill(self):
        print("Coding")

c=Child()
c.skills()
c.ownskill()