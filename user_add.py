from db_connection import connect_db, Error

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is the name of the new user? ").title()
            email = input("What is the new user's email address? ")
            phone = input("What is the new user's phone number? ")

            new_user = (name, email, phone)

            query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(query, new_user)

            conn.commit()
            print(f"The new user {name}, {email}, {phone} has been created successfully!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_user()