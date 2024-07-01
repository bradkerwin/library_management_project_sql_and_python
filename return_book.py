from db_connection import connect_db, Error

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            book_return = input("What book are you returning? ")
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s;"
            cursor.execute(query, (book_return,))

            id, title, author, availability = cursor.fetchall()[0]
            print(f"{id}: Thank you for returning the book {title} by {author}. Have a great day!")

            if availability == "not available":
                availability = "available"
                change_availability = (availability, title)

                return_query = "UPDATE books SET availability = %s WHERE title = %s;"
                cursor.execute(return_query, change_availability)
                
                book_id = id
                cursor = conn.cursor()
                delete_query = 'DELETE FROM borrowed_books WHERE book_id = %s;'
                cursor.execute(delete_query, (book_id,))
                conn.commit()
                
                print(f"Thank you for returning {book_return}. Have a great day.")

            elif availability == "available":
                print(f"There's no record of {book_return} ever being rented from here.")

        except IndexError:
            print("It appears this book was never here. You may want to confirm where you rented it from.")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn == conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    return_book()