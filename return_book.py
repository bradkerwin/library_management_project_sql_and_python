from db_connection import connect_db, Error

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            book_return = input("What book are you returning? ")
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s;"
            cursor.execute(query, (book_return,))

            id, title, author = cursor.fetchall()
            print(f"{id}: Thank you for returning the book {title} by {author}. Have a great day!")

            if availability == 0:
                availability = 1
                change_availability = (availability, title)

                return_query = "UPDATE books SET availability = %s WHERE title = %s;"
                cursor.execute(return_query, change_availability)

                user_id = input("Please enter your user ID ")
                book_id = id

            elif availability == 0:
                print(f"There's no record of {book_return} ever being rented from here.")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn == conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    return_book()