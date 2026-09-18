import mysql.connector

def print_user(user):

    config = {
        "host": "127.0.0.1",
        "port": 3306,        # <- Sin comillas (entero)
        "database": "hello_mysql",
        "user": "root",
        "password": "Admin123" 
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM users where name=%s;"
    print(query)
    cursor.execute(query, (user,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()

print_user("Brais")
#print_user("'; UPDATE users SET age = 15, WHERE user_id=1; -- ")