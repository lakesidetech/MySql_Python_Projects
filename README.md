
# MySql_Python_Projects
## Perquisites
* Install Python 3 - https://www.python.org/downloads/
* Install MySQL - https://dev.mysql.com/downloads/installer/
* Check if you have administration or root priviledges
* Install mysql Python Connector
* pip install mysql-connector-python==8.0.17


## First establish a connection to the employee1 db
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth",
  database="employees1"  
)


![create a database](https://user-images.githubusercontent.com/17750481/111886899-6bda1280-89e2-11eb-895c-f7aa50d18044.JPG)

## Create a cursor object via the cursor() method
mycursor=mydb.cursor()


## use a query statement to create a database
## Create the database
**mycursor.execute("CREATE DATABASE employees1")**
# display your list of databases
* mycursor.execute("SHOW DATABASES")

## loop through your databases
for x in mycursor:
![image](https://user-images.githubusercontent.com/17750481/111898258-f435d300-8a35-11eb-8d03-62e8005e1ea1.png)
  print(x)

## Closing the connection
mydb.close()

