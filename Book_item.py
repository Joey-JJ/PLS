class Book_item(object):
    def __init__(self, book, id) -> None:
        self.book: object = book
        self.id = id
        self.loaned_out = False

    def to_dict(self) -> dict:
        dict = self.__dict__.copy()
        dict['book'] = self.book.__dict__.copy()
        return dict
