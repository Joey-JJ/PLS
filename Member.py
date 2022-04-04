from Person import Person


class Member(Person):
    def __init__(self, number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number) -> None:
        super().__init__(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)
        self.books_rented = []
        self.num_rented = len(self.books_rented)

    """
    TODO: Functions to add
    Catalog
    - To check the catalog (list of books)
    - To search a book in the catalog
    
    Book items:
    - To see the list of book items in the library
    - To search a book item and its availability in the catalog library
    - To loan a book item
    - To return a loaned book item
    """