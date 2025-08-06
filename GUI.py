# What is Tkinter?

# Tkinter is Python's Studard GUI (Graphical Uer Interface) Library
# It Provides tools to Create Windows, buttons, lables, text boxes, etc

# Basic Tkinter Window

# import tkinter as tk

# root=tk.Tk()
# root.title("Credo Systemz")
# root.geometry("200x100")
# root.mainloop()

#Label Example

# import tkinter as tk

# root=tk.Tk()
# root.title("Credo Systemz")
# root.geometry("400x400")

# label=tk.Label(root, text="Welcome to Credo Systemz - Python Session")
# label.pack()
# root.mainloop()


# Button Clicke Example

# import tkinter as tk 

# def clicked():
#     print("Python Button was Clicked!!")


# root=tk.Tk()
# root.title("Credo Systemz")
# root.geometry("400x400")

# button=tk.Button(root, text="Click Me", command=clicked)
# button.pack()
# root.mainloop()


# Entry Box Input

# import tkinter as tk

# def get_input():
#     print("User Name - ", entry.get())
    
    
# root=tk.Tk()
# root.title("Entry Box Input")
# root.geometry("400x400")

# entry=tk.Entry(root)
# entry.pack()


# tk.Button(root, text="Submit", command=get_input).pack()
# root.mainloop()




# Simple Calculator 


import tkinter as tk 

def add():
    result=int(num1.get())+int(num2.get())
    output.config(text="Result : "+str(result))
    
def sub():
    result=int(num1.get())-int(num2.get())
    output.config(text="Result : "+str(result))

def mul():
    result=int(num1.get())*int(num2.get())
    output.config(text="Result : "+str(result))
    
    
    
    

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")
num1=tk.Entry(root)
num1.pack()
num2=tk.Entry(root)
num2.pack()



tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Sub", command=sub).pack()
tk.Button(root, text="Mul", command=mul).pack()
output=tk.Label(root, text="")
output.pack()
root.mainloop()