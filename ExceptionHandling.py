#  What is Exception Handling 
# Exception Handling is a way to handle runtime errors in your code without crashing the program

# Why use it?
# To Catch and handle error gracefully
# e.g., divide by zero, file not found, wrong input

# try:
    # code that may raise an exception
# except ExceptionType:
    # Code to handle the exception 
# finally:
    # Code that always runs (optional)

# else:
    # Code if no exception occurs (optional)

# Type
# try, except, else, finally, raise, assert

# Divide by Zero

# try:
#     x=10/2
#     print(x)
# except ZeroDivisionError:
#     print("Can't divide by zero")


# x=2/0
# print(x)

# File Not Found 

# try:
#     f=open("file.txt")
# except FileNotFoundError:
#     print("File Not Found")

# Input Validation 

# try:
#     age=int(input("Enter age : "))
#     print(age)
# except ValueError:
#     print("Please enter a valid number ")


# Index Error 

# try:
#     a=[1,2,3]
#     print(a[1])
# except IndexError:
#     print("Index out of range")

# Type Error

try:
    a=5+5 
    print(a)
except TypeError:
    print("Cannot add string and interger")
finally:
    print("Thank You")

