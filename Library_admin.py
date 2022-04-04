from Person import Person


class Library_admin(Person):
    def __init__(self, number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number) -> None:
        super().__init__(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)

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