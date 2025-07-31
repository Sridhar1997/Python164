# File 

# open('filename', 'mode')

# Mode - r - read, w - write, a - append, x - create, b - binary mode, t - text mode 

# Create a File and Write Text

# f=open("file1.txt", "w")
# f.write("Welcome to Credo Systemz - Python Class - 164")
# f.close()

# Read a File 

# f=open("file1.txt", "r")
# print(f.read())
# f.close()


# Append Data to an Existing File

# f=open("file1.txt", "a")
# f.write("\n Core Python, OOPS Python, GUI, Collections, Database")
# f.close()

# Read File Line by Line

# f=open("file1.txt", "r")

# for line in f:
#     print(line.strip())
# f.close()


# Uisng with statement (Auto Close)

# with open("file1.txt", "r") as f :
#     print(f.read())

# With Multiple Lines 

# lines=["HTML\n", "CSS\n", "JavaScript\n", "Django\n", "Flask\n"]

# with open("file1.txt", "w") as f:
#     f.writelines(lines)


# f=open("file1.txt", "r")
# print(f.read(10))
# f.close()



# Delete a File

# import os
# os.remove("file.txt")


# Rename a File 

import os
os.rename("file1.txt", "sridhar.txt")