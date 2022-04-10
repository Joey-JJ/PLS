from Catalog import Catalog
from Book_item import Book_item


class Library_stock(object):
    # Stock is a list of book items that are currrently in the library
    stock = []

    def create_stock():
        """Creates 3 book items per book in the catalog. Also assign unique ID."""
        unique_id = 1
        for book in Catalog.books:
            for _ in range(3):
                book_item = Book_item(book, unique_id)
                Library_stock.stock.append(book_item)
                unique_id+=1


    def list_stock():
        for book_item in Library_stock.stock:
            print(f'{book_item.id}. {book_item.book.title} by {book_item.book.author}. Loaned out: {book_item.loaned_out}')


    def search_book_item():
        query = input('Enter (part of) the book title or author: ')
        results = [book_item for book_item in Library_stock.stock if query.lower() in book_item.book.title.lower() or query.lower() in book_item.book.title.lower()]
        print('The following books were found: ')
        if len(results) > 0:
            for res in results:
                print(f'ID: {res.id}. {res.book.title}" by {res.book.author}. Loaned out: {res.loaned_out}')
        else:
            print('None')
        input('Press \'Enter\' to continue.')

    
    def edit_book_item_id():
        book_item = Library_stock.get_book_item()
        if book_item == None:
            return
        while True:
            try:
                new_id = int(input('Enter the new ID: '))
                for book_item in Library_stock.stock:
                    if book_item.id == new_id:
                        print('ID already taken, please try again.')
                        raise ValueError("Invalid ID")
            except:
                print('Invalid input, please try again')
            else:
                book_item.id = new_id
                print('Changes saved.')
                break


    def delete_book_item():
        item = Library_stock.get_book_item()
        if item == None:
            return
        Library_stock.stock.remove(item)
        print('Deleted book item\n')


    def add_book_item():
        if len(Catalog.books) == 0:
            print('You can not add any book items if there are no books in the catalog. Please load in books first.')
            return
        for index, book in enumerate(Catalog.books):
            print(f'{index + 1}. {book.title} by {book.author}')
        while True:
            try:
                book_num = int(input('Enter the number of the book you want to create a book item for: '))
                for index, book in enumerate(Catalog.books):
                    if index + 1 == book_num:
                        book_to_use = book
                
            except:
                print('Invalid input, please try again.\n')
            else:
                id_to_use = Library_stock.check_id()
                Library_stock.stock.append(Book_item(book_to_use, id_to_use))
                print('Book item added')
                break


    def check_id():
        while True:
            try:
                new_id = int(input('Enter the (new) ID: '))
                for book_item in Library_stock.stock:
                    if book_item.id == new_id:
                        raise ValueError('ID already taken')
            except:
                print('ID already taken or invalid input. Please try again.\n')
            else:
                return new_id

    
    def get_book_item():
        id = input('\nEnter the ID of the book item: ')
        for book_item in Library_stock.stock:
            if str(book_item.id) == id:
                return book_item
        print('Could not find book item')
        return None
