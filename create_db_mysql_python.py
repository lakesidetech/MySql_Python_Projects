#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python==8.0.17


# In[2]:


import mysql.connector
import csv


# In[4]:


# Create cursor object
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth",
  database="employees1"  
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE employees1")


# In[18]:


print(mydb)


# In[33]:


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[5]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth",
  database="employees1"  
)
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS employees(name VARCHAR(255), address VARCHAR(255))")
sql_employee = "INSERT INTO employees (name, address) VALUES (%s, %s)"
val = ("Jerry Alberts", "Highway 21")
mycursor.execute(sql_employee, val)
mydb.commit()

print(mycursor.rowcount, "Record Successfully Inerted.")


# In[ ]:




