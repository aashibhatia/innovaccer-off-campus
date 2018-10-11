import mysql.connector
import reminder

def store_in_database(email, tv_series):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='reminder'
    )

    # print(mydb)
    mycursor = mydb.cursor()
    # Create database 'reminder'
    # mycursor.execute("CREATE DATABASE reminder")
    mycursor.execute("CREATE TABLE customer (email VARCHAR(255), series VARCHAR(255))")

    # check existing databases
    # mycursor.execute("SHOW DATABASES")
    # for x in mycursor:
        # print(x)

    sql = "INSERT INTO reminder (email, series) VALUES (%s, %s)"
    val = (email, tv_series)
    mycursor.execute(sql, val)

    # Commit current transaction
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
