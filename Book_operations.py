from book_add import add_book
from book_fetch import fetch_books, fetch_single_book
from return_book import return_book
from rent_book import rent_book

def book_operations():
    while True:
        user = input('''
Book Operations:
1. Add a new book 
2. Borrow a book 
3. Return a book
4. Search for a book
5. Display all books
6. Return to main menu                     
''')
        if user == '1':
            add_book()
        elif user == '2':
            rent_book() 
        elif user == '3':
            return_book()
        elif user == '4':
            fetch_single_book()
        elif user == '5':
            fetch_books()
        elif user == '6':
            break
        else:
            print("Invalid entry. Please try again")

if __name__ == "__main__":
    book_operations()