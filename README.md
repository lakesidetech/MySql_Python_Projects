
# MySql_Python_ProjectsPerquisites
1.	Install Python 
2.	Check if you have administration or root priviledges
3.	Install mysql Python Connector
4.	pip install mysql-connector-python==8.0.17

import mysql.connector

#first establish a connection to the employee1 db

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth",
  database="employees1"  
)

# Create a cursor object via the cursor() method
mycursor=mydb.cursor()


#use a query statement to create a database
#Create the database
mycursor.execute("CREATE DATABASE employees1")
#display your list of databases![create a database](https://user-images.githubusercontent.com/17750481/111886899-6bda1280-89e2-11eb-895c-f7aa50d18044.JPG)

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#Closing the connection
mydb.close()

mydb.close()

