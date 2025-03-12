import sqlite3

connection  = sqlite3.connect("student.db")
cursor      = connection.cursor()

## create the table
tableInfo="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(tableInfo)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Display all the records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
