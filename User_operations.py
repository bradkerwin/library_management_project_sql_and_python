from user_add import add_user
from user_fetch import fetch_users, fetch_single_user

def user_operations():
    while True:
        user = input('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Return to main menu
''')
        if user == '1':
            add_user()
        elif user == '2':
            fetch_single_user()
        elif user == '3':
            fetch_users()
        elif user == '4':
            break
        else:
            print("Invalid entry. Please try again.")