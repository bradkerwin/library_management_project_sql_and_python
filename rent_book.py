from db_connection import connect_db, Error
from datetime import date

def rent_book():
    conn = connect_db()
    if conn is not None:
        try:
            rental = input("What book would you like to rent today? ").title()
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(query, (rental,))

            book_id, title, author, availability = cursor.fetchall()[0]
            print(f"{book_id}: The book {title} by {author} is available to rent!")

            if availability == "available":
                availability = "not available"
                change_availability = (availability, title)

                rental_query = "UPDATE books SET availability = %s WHERE title = %s;"
                cursor.execute(rental_query, change_availability)
                
                confirm_user_id = input("Please enter your user ID ")
                rental_date = date.today()
                rental_info = (confirm_user_id, book_id, rental_date)

                add_to_borrowed_query = 'INSERT INTO borrowed_books(user_id, book_id, borrow_date) VALUES(%s, %s, %s);' 
                cursor.execute(add_to_borrowed_query, rental_info)
                conn.commit()
                
                print(f"You have now rented {rental}.")

            elif availability == "not available":
                print(f"{rental} is currently being rented.")

        except IndexError:
            print("It appears we do not have that book in stock.")

        except Error as e:
            print(f"Error: {e}")    

        finally:
            if conn == conn.is_connected():
                cursor.close()
                conn.close() 

if __name__ == "__main__":
    rent_book()