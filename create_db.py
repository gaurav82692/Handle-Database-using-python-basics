import mysql.connector

mydb= mysql.connector.connect(host="localhost",
    user="root",
    passwd="9696")
print(mydb )
mycursor = mydb.cursor()
mycursor.execute("Create database Employee")     #to create database
mycursor.execute("show databases")
for x in mycursor:
	print(x)