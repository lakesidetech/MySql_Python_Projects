#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python==8.0.17


# In[5]:


import mysql.connector
import csv


# In[2]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth"
)

mycursor = mydb.cursor()


# In[9]:


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Academics30")


# In[4]:


print(mydb)


# In[5]:


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[6]:


mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="academics30"
)
#instantiate cursor
mySql_Create_Table_Query1 = """CREATE TABLE IF NOT EXISTS College1 ( 
                             College_Id int(11) NOT NULL,
                             College_Name varchar(250) NOT NULL,
                             College_Address varchar(250) NOT NULL,
                             College_City varchar(100),
                             College_Country varchar(100),
                             PRIMARY KEY (College_Id)) """

mycursor=mydb.cursor()
result = mycursor.execute(mySql_Create_Table_Query1)
mydb.commit
print("College1 Table created successfully ")


# In[1]:


import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="academics30"
)

mycursor=mydb.cursor()

#create Professor table
mySql_Create_Table_Query2="""CREATE TABLE IF NOT EXISTS professor(
                            Teacher_id int NOT NULL, 
                            Teacher_Name text, 
                            School_id int NOT NULL, 
                            date_joined text,
                            speciality text, 
                            salary int, 
                            experience int,
                            PRIMARY KEY (Teacher_id))"""

mmycursor=mydb.cursor()
result = mycursor.execute(mySql_Create_Table_Query2)
mydb.commit
print("professor Table created successfully ")
print(mycursor.rowcount, "record was inserted.")
mycursor.close()


# In[ ]:





# In[4]:


import csv
mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="academics30"
)
#instantiate cursor
mySql_Create_Table_Query22 = """CREATE TABLE IF NOT EXISTS Students ( 
                             StudentId int(11) NOT NULL,
                             StudentName varchar(100) NOT NULL,
                             Student_email varchar(100) NOT NULL,
                             college_id int(11),
                             date_joned DATE,
                             major_taken varchar(100),
                             college_level varchar(100),
                             PRIMARY KEY (StudentId)) """

mycursor=mydb.cursor()
result = mycursor.execute(mySql_Create_Table_Query22)
mydb.commit()
print("Students Table created successfully ...")


# In[13]:


import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="academics30"
)

mycursor=mydb.cursor()

#  Insert college1 records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\College_info.csv', 'r') as collegerec:
    c_reader = csv.reader(collegerec)

    next(c_reader)  # dkip first ecord
    for rec in c_reader:
        mycursor.execute(
            "INSERT IGNORE INTO college1(College_id, College_Name, College_Address, College_city, College_country) VALUES(%s, %s, %s, %s, %s)", rec)
        mydb.commit()
print("College records added")


# In[15]:


import mysql.connector,csv

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="academics30"
)

mycursor=mydb.cursor()


#  Insert professor records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\professor.csv', 'r') as profrec:
    p_reader = csv.reader(profrec)

    next(p_reader)  # dkip first ecord
    for rec in p_reader:
        mycursor.execute(
            "INSERT IGNORE INTO professor(teacher_id, Teacher_Name, School_id, Date_joined, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s,%s)", rec)
        mydb.commit()
print("Professor records added")


# In[14]:


import mysql.connector,csv

mydb = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "ruth",
      database="academics30"
)

mycursor=mydb.cursor()

#  Insert studenst records from csv file
with open('C:\\Users\\user\\Desktop\\python-files\\students_info.csv', 'r') as srec:
    s_reader = csv.reader(srec)

    next(s_reader)  # dkip first ecord
    for rec in s_reader:
        mycursor.execute(
            "INSERT IGNORE INTO students(Studentid, StudentName, Student_Email, College_id, Date_joned, Major_taken, College_Level) VALUES (%s, %s, %s, %s, %s, %s, %s)", rec)
        mydb.commit()
print("Student records added")


# In[ ]:




