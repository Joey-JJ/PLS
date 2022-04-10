class Book_item(object):
    def __init__(self, book, id) -> None:
        self.book: object = book
        self.id = id
        self.loaned_out = False
