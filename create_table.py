import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='9696',
                             db='employee')
mycursor = connection.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("select * from test2.customers")
