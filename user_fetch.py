from db_connection import connect_db, Error

def fetch_users():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users;"
            cursor.execute(query)

            id, name , email, phone = cursor.fetchall()
            print(f"{id} {name} {email} {phone}")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def fetch_single_user():
    conn = connect_db()

    if conn is not None:
        try:
            users_name = input("Enter the name of the user you are searching for ").title()
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE name = %s;"
            cursor.execute(query, (users_name,))

            id, name , email, phone = cursor.fetchall()[0]
            print(f"{id} {name} {email} {phone}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

#fetch_single_user()

if __name__ == "__main__":
    fetch_users()