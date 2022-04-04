from Book import Book


class Book_item(object):
    def __init__(self, book: object) -> None:
        self.book = book
        self.current_stock = 3