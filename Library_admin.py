from User_account import User_account


class Library_admin(User_account):
    def create_account(self):
        user_name = input('Enter the username: ')
        password = input('Enter the password: ')
        return User_account(user_name, password)

    """
    TODO: Functions to add
    Members:
    - See the list of members
    - Add, edit, delete members
    - Check status of book items that are currently loaned
    - Load and add a list of members to the system, all at once (using a csv file)

    Catalog
    - To check the catalog (list of books)
    - To add, edit, and delete a book to/from the catalog
    - To search a book in the catalog
    - To load and add a list of books to the catalog, all at once (using a json file)
    
    Book items:
    - To see the list of book items in the library
    - To add, edit, and delete a book item to/from the library
    - To search a book item and its availability in the catalog library
    - To lend a book item to a member
    
    System administration
    - To make backups of the system
    - To restore a specific backup of the system
    """