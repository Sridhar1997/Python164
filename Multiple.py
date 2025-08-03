# Person + Student -> Result  


# class Person:
#     def personInfo(self):
#         print("Sridhar Raj P")

# class Student:
#     def studentInfo(self):
#         print("101")
    
# class Result(Person, Student):
#     def showReult(self):
#         print("Pass")

# r=Result()
# r.personInfo() 
# r.showReult()
# r.studentInfo()



# class Father:
#     def FatherInfo(self):
#         print("Tall")

# class Mother:
#     def MotherInfo(self):
#         print("Intelligent")
        
# class Child(Father, Mother):
#     def ChildInfor(self):
#         print("Tall, Intelligent")

# c=Child()
# c.FatherInfo() 
# c.MotherInfo() 
# c.ChildInfor()


class Animal:
    def walk(self):
        print("Animal can walk")

class Bird:
    def fly(self):
        print("Bird can fly")

class Bat(Animal, Bird):
    def sleep(self):
        print("Bat sleeps")
        
        
b=Bat()
b.walk()
b.fly()
b.sleep()