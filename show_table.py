import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='9696',
                             db='employee')
mycursor = connection.cursor()

mycursor.execute("select * from customers")
for x in mycursor:
  print(x)