# class Animal:
#     def sound(self):
#         print("Animals make sounds")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")
        
# d=Dog()
# d.sound()
# d.bark()


# class Person:
#     def __init__(self):
#         self.name="Sridhar"
    
# class Student(Person):
#     def show(self):
#         print("Welcome "+self.name)

# s=Student()
# s.show()


class Parent:
    def greet(self):
        print("Hello from Parent")
    
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c=Child()
c.greet()