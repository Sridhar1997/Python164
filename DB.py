# import mysql.connector 

# db=mysql.connector.connect(
    
#     host="localhost",
#     user="root",
#     password=""
#     )

# cursorvalue=db.cursor()

# cursorvalue.execute("CREATE DATABASE credodatabase")


#########################################################

# import mysql.connector 

# db=mysql.connector.connect(
    
#     host="localhost",
#     user="root",
#     password=""
#     )

# cursorvalue=db.cursor()
# cursorvalue.execute("SHOW DATABASES")

# for i in cursorvalue:
#     print(i)


###########################################################


import mysql.connector 

db=mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="",
    database="credodatabase"
    )

cursorvalue=db.cursor()

cursorvalue.execute("SELECT address FROM teacher")

answer=cursorvalue.fetchall()

# answer=cursorvalue.fetchone()

for x in answer:
    print(x)

# sql="INSERT INTO teacher (name, address) VALUES (%s, %s)"
# val=("Sridhar", "CHENNAI - OMR")

# cursorvalue.execute(sql, val)
# db.commit()
# print(cursorvalue.rowcount,  " Record Inserted.")

# cursorvalue.execute("CREATE TABLE teacher(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# cursorvalue.execute("SHOW TABLES")

# for i in cursorvalue:
#     print(i)

# cursorvalue.execute("CREATE TABLE student (name VARCHAR(255), address VARCHAR(255))")

