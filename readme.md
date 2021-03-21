# Introduction
prerequisite
Install Python
https://www.python.org/downloads/
Install MySQL
https://dev.mysql.com/downloads/installer/
Check if you have administration or root priviledges
Install mysql Python Connector
pip install mysql-connector-python==8.0.17

# General Information

# Setup


#first establish a connection to the employee1 db
import mysql.connector

mydb = mysql.connector.connect( host="localhost", user="root", password="ruth", database="employees1"
)
Create a cursor object via the cursor() method
mycursor=mydb.cursor()

#use a query statement to create a database #Create the database mycursor.execute("CREATE DATABASE employees1") #display your list of databases
mycursor.execute("SHOW DATABASES")

for x in mycursor: print(x)

#Closing the connection mydb.close()

mydb.close()


