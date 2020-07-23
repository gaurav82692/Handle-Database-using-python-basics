import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='9696',
                             db='business')
mycursor = connection.cursor()

sql = "INSERT INTO customers (id,name, address) VALUES (%s,%s, %s)"
val = (str(id),input("enter name : "), input("enter address : "))
mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")


