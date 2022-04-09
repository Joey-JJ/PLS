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


    def list_books():
        for index, book in enumerate(Catalog.books):
            print(f'{index + 1}. {book.title} by {book.author}')


    def search():
        query = input('Enter (part of) the book title or author: ')
        results = [book for book in Catalog.books if query.lower() in book.title.lower() or query.lower() in book.title.lower()]
        print('The following books were found: ')
        if len(results) > 0:
            for res in results:
                print(f'"{res.title}" by {res.author}')
        else:
            print('None')


    def get_book():
        title = input('Enter the title of the book you want to edit: ').lower()
        book_to_edit = None
        for book in Catalog.books:
            if book.title.lower() == title:
                book_to_edit = book
                return book
        if book_to_edit == None:
            print('Book not found')
            return None


    def add_book():
        author = input('Enter the author: ')
        country = input('Enter the country: ')
        imageLink = input('Enter the image link: ')
        language = input('Enter the language: ')
        link = input('Enter the link: ')
        pages = input('Enter the amount of pages: ')
        title = input('Enter the title: ')
        isbn = input('Enter the ISBN: ')
        year = input('Enter the year: ')
        
        new_book = Book(author, country, imageLink, language, link, pages, title, isbn, year)
        Catalog.books.append(new_book)
        input('Book added, press \'enter\' to continue.')


    def edit_book():
        book_to_edit = Catalog.get_book()
        if book_to_edit == None:
            return
        while True:
            to_edit = input(
                'What would you like to edit?\n' + \
                '[1] Author\n' + \
                '[2] Country\n' + \
                '[3] Image link\n' + \
                '[4] Language\n' + \
                '[5] Link\n' + \
                '[6] Pages\n' + \
                '[7] Title\n' + \
                '[8] ISBN\n' + \
                '[9] Year\n'
            )
            if to_edit == '1':
                new_author = input('Enter the author you would like to change it into: ')
                book_to_edit.author = new_author
                print('Change saved')
                return
            elif to_edit == '2':
                new_country = input('Enter the country you would like to change it into: ')
                book_to_edit.country = new_country
                print('Change saved')
                return
            elif to_edit == '3':
                new_imagelink = input('Enter the image link you would like to change it into: ')
                book_to_edit.imageLink = new_imagelink
                print('Change saved')
                return
            elif to_edit == '4':
                new_language = input('Enter the language you would like to change it into: ')
                book_to_edit.language = new_language
                print('Change saved')
                return
            elif to_edit == '5':
                new_link = input('Enter the link you would like to change it into: ')
                book_to_edit.link = new_link
                print('Change saved')
                return
            elif to_edit == '6':
                new_pages = input('Enter the number of pages you would like to change it into: ')
                book_to_edit.pages = new_pages
                print('Change saved')
                return
            elif to_edit == '7':
                new_title = input('Enter the title you would like to change it into: ')
                book_to_edit.title = new_title
                print('Change saved')
                return
            elif to_edit == '8':
                new_isbn = input('Enter the ISBN you would like to change it into: ')
                book_to_edit.ISBN = new_isbn
                print('Change saved')
                return
            elif to_edit == '9':
                new_year = input('Enter the year you would like to change it into: ')
                book_to_edit.year = new_year
                print('Change saved')
                return
            else:
                print('Please enter a valid option...')


    def delete_book():
        book_to_delete = Catalog.get_book()
        if book_to_delete == None:
            return
        for book in Catalog.books:
            if book.title == book_to_delete.title:
                Catalog.books.remove(book)
                print('\nBook deleted. Press \'Enter\' to continue\n')
