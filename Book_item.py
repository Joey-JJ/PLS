from Book import Book


class Book_item(Book):
    def __init__(self, author, country, imageLink, language, link, pages, title, ISBN, year) -> None:
        super().__init__(author, country, imageLink, language, link, pages, title, ISBN, year)
