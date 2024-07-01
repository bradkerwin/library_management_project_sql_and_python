from Book_operations import book_operations
from User_operations import user_operations

def main():
    while True:
        user = input('''
    Welcome to the Library Management System with Database Integration!
    ****
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Quit                 
    ''')
        if user == '1':
            book_operations()
        elif user == '2':
            user_operations()
        elif user == '3':
            print("Thank you for using our Library Management System. Have a great day.")
            break
        else:
            print("Invalid entry. Please try again.")

if __name__ == "__main__":
    main()