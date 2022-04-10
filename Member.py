from Library_stock import Library_stock
from Loan_item import Loan_item
from Person import Person


class Member(Person):
    def __init__(self, number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number) -> None:
        super().__init__(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)
        self.loan_items = []


    def loan_book_item(self):
        Library_stock.list_stock()
        book_item = Library_stock.get_book_item()
        book_item.loaned_out = True
        loan_item = Loan_item(book_item)
        self.loan_items.append(loan_item)
        day = loan_item.return_due.day
        month = loan_item.return_due.month
        year = loan_item.return_due.year
        date = f'{day}-{month}-{year}'
        print(f'Loaned book item. Please return it on: {date}')


    def return_book_items(self):
        if len(self.loan_book_item) == 0:
            print('There are no books to return.')
            return
        elif len(self.loan_items) > 1:
            print('Which book do you want to return? Select the number')
            for index, book in enumerate(self.loan_items):
                print(f'[{index + 1}] {book.book_item.book.title}')
            while True:
                try:
                    pass
                except:
                    print('Please enter a valid option')

                
