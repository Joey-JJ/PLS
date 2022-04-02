import json
from Book import Book


class Catalog(object):
    books = []

    def load_books():
        with open('Books.json', 'r') as f:
            books_list = json.load(f)
        for book in books_list:
            book_properties = []
            for key, value in book.items():
                book_properties.append(value)
            Catalog.books.append(Book(
                book_properties[0], 
                book_properties[1],
                book_properties[2],
                book_properties[3],
                book_properties[4],
                book_properties[5],
                book_properties[6],
                book_properties[7],
                book_properties[8]))

    def print_books():
        number = 1
        for book in Catalog.books:
            print(f'{number}. {book.title} by {book.author}')
            number += 1