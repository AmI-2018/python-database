import pymysql

if __name__ == "__main__":
    # 1. prepare the SQL query
    sql = "select * from todo"

    # 2. create the connection and connect
    connection = pymysql.connect(user="root", password="", host="localhost", database="todolist")

    # 3. get a cursor
    cursor = connection.cursor()
    # 4. execute the query
    cursor.execute(sql)
    # 5. fetch the results from the DB
    result = cursor.fetchall()
    # 6. print the results
    print(result)
    # 7. close the cursor
    cursor.close()

    # another SQL query, with placeholders
    sql2 = "insert into todo(description, urgent) values (%s, %s)"
    my_description = "go to the lab"
    my_urgency = 1

    # get another cursor
    cur = connection.cursor()
    # execute the query
    cur.execute(sql2, (my_description, my_urgency))
    # submit the changes
    connection.commit()
    # close the second curso
    cur.close()

    # 8. close the connection
    connection.close()
