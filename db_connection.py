import mysql.connector 
from mysql.connector import Error 

def connect_db():
    db_name = "library_management"
    user = "root" 
    password = "TomJ0@nz"
    host = "localhost" 

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connected to MySQL database successful!")
            return conn

    except Error as e:
        print(e)
        return None
#connect_db()