import json
from Book import Book


class Catalog(object):
    books = []

    def load_books(filename: str):
        with open(filename, 'r') as f:
            books_list = json.load(f)
        for book in books_list:
            book_properties = []
            for value in book.values():
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
    
    def search():
        query = input('Enter (part of) the book title or author: ')
        results = []
        for book in Catalog.books:
            if query.lower() in book.title.lower() or query.lower() in book.title.lower():
                results.append(book)
        print('The following books were found: ')
        if len(results) > 0:
            for res in results:
                print(f'"{res.title}" by {res.author}')
        else:
            print('None')