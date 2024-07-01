from db_connection import connect_db, Error

def rent_book():
    conn = connect_db()
    if conn is not None:
        try:
            rental = input("What book would you like to rent today? ").title()
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(query, (rental,))

            id, title, author, availability = cursor.fetchall()
            print(availability)
            print(f"{id}: The book {title} by {author} is available to rent!")

            if availability == 1:
                availability = 0
                change_availability = (availability, title)

                rental_query = "UPDATE books SET availability = %s WHERE title = %s;"
                cursor.execute(rental_query, change_availability)

                user_id = input("Please enter your user ID ")
                book_id = id

            elif availability == 0:
                print(f"{rental} is currently being rented.")

        except Error as e:
            print(f"{e}")

        finally:
            if conn == conn.is_connected():
                cursor.close()
                conn.close() 

if __name__ == "__main__":
    rent_book()