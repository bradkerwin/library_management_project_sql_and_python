from db_connection import connect_db, Error

def fetch_books():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books;"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def fetch_single_book():
    conn = connect_db()

    if conn is not None:
        try:
            book_title = input("What is the title of the book you are looking for? ")
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s;"
            cursor.execute(query, (book_title,))

            id, title, author, availability = cursor.fetchall()[0]
            print(f"{id} {title} {author} {availability}")

        except IndexError:
            print("Sorry, we do not have that book in stock right now.")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


if __name__ == "__main__":
    fetch_books()