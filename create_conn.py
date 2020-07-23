import mysql.connector

mydb= mysql.connector.connect(host="localhost",
    user="root",
    passwd="9696")
print(mydb )