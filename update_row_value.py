import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='9696',
                             db='business')
mycursor = connection.cursor()

mycursor.execute("select * from business.business")

for x in mycursor:
  print(x)

print(" ")



sql = "UPDATE business SET address = 'gggg' WHERE address = 'basaratpur'"

mycursor.execute(sql)

connection.commit()

print(mycursor.rowcount, "record(s) affected")

print(" ")

mycursor.execute("select * from business.business")

for x in mycursor:
  print(x)