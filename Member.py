from Library_stock import Library_stock
from Loan_item import Loan_item
from Person import Person
import datetime


class Member(Person):
    def __init__(self, number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number) -> None:
        super().__init__(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)
        self.loan_items = []

    
    def to_dict(self) -> dict:
        dict = self.__dict__.copy()
        loan_items = []
        for loan_item in self.loan_items:
            loan_items.append(loan_item.to_dict())
        dict['loan_items'] = loan_items
        return dict


    def loan_book_item(self):
        if len(self.loan_items) >= 3:
            print('You can loan up to 3 books at once. Please return a book before trying to loan again.')
            return
        Library_stock.list_stock()
        id = input('\nEnter the ID of the book item: ')
        book_found = False
        for book in Library_stock.stock:
            if str(book.id) == id and not book.loaned_out:
                book_item = book
                book_found = True
        if not book_found:
            print('Could not find book item or book already loaned out.')
            return
        book_item.loaned_out = True
        loan_item = Loan_item(book_item)
        self.loan_items.append(loan_item)
        date = loan_item.return_due.strftime('%d-%m-%Y')
        print(f'Loaned book item. Please return it on: {date}')


    def return_book_items(self):
        if len(self.loan_items) == 0:
            print('There are no books to return.')
            return
        elif len(self.loan_items) == 1:
            self.loan_items[0].returned_on = datetime.date.today()
            if self.loan_items[0].check_fine():
                print('The book was returned too late.')
            self.loan_items[0].book_item.loaned_out = False
            for book_item in Library_stock.stock:
                if book_item.id == self.loan_items[0].book_item.id:
                    book_item.loaned_out = False 
            self.loan_items = []
            print('Returned the book.')
        elif len(self.loan_items) > 1:
            print('Which book do you want to return? Select the number')
            for index, book in enumerate(self.loan_items):
                print(f'[{index + 1}] {book.book_item.book.title}')
            while True:
                try:
                    book_index = int(input('Enter the number here: ')) - 1
                except:
                    print('Please enter a valid option')
                else:
                    self.loan_items[book_index].returned_on = datetime.date.today()
                    if self.loan_items[book_index].check_fine():
                        print('The book was returned too late.')
                    for book_item in Library_stock.stock:
                        if book_item.id == self.loan_items[book_index].book_item.id:
                            book_item.loaned_out = False 
                    self.loan_items.remove(self.loan_items[book_index])
                    print('Returned the book.')
                    break
