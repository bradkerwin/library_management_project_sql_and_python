from db_connection import connect_db, Error

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is the title of the book? ").title()
            author = input("Who is the author of the book? ").title()

            new_book = (title, author)

            query = "INSERT INTO books (title, author) VALUES (%s, %s)"
            cursor.execute(query, new_book)

            conn.commit()
            print(f"The new book {title} by {author} has been added successfully!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_book()