import pymysql

server_name = 'http://localhost:2000'
user = 'root'
password = 'pass'
name = 'test'
charset = 'utf8mb4'
cursor_type = pymysql.cursors.DictCursor

connection = pymysql.connect(host=server_name,
                             user=user,
                             password=password,
                             db=name,
                             charset=charset,
                             cursorclass=cursor_type)

try:
    cursorObj = connection.cursor()

    # SQL query string
    sql_query = "CREATE TABLE Details(Email varchar(32), TV-Series varchar(32))"

    # Execution of SQL query
    cursorObj.execute(sql_query)

    sql_query = "show tables"
    cursorObj.execute(sql_query)

    # Fetch rows
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Exception occurred: {}".format(e))

finally:
    connection.close()
