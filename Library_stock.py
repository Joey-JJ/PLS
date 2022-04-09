from Catalog import Catalog
from Book_item import Book_item


class Library_stock(object):
    # Stock is a list of book items that are currrently in the library
    stock = []

    def create_stock():
        """Creates 3 book items per book in the catalog. Also assign unique ID."""
        for id, book in enumerate(Catalog.books):
            for _ in range(3):
                book_item = Book_item(
                    book.author,
                    book.country,
                    book.imageLink,
                    book.language,
                    book.link,
                    book.pages,
                    book.title,
                    book.ISBN,
                    book.year,
                    id + 1)
                Library_stock.stock.append(book_item)

    
    def list_stock():
        for book_item in Library_stock.stock:
            print(f'{book_item.id}. {book_item.title} by {book_item.author}')
