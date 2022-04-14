import time
import datetime as dt
from Book import Book
from Book_item import Book_item
from Catalog import Catalog
from JSON import JSON_handler
from Library_accounts import Library_accounts
from Library_stock import Library_stock
from Loan_item import Loan_item
from Member import Member


class System(object):
    def save_all_data():
        System.save_members_data()
        System.save_library_stock_data()
        System.save_catalog_data()
    

    def load_all_data():
        System.load_members_data()
        System.load_library_stock_data()
        System.load_catalog_data()


    def make_back_up():
        members_data = JSON_handler.load_file('member_data')
        catalog_data = JSON_handler.load_file('catalog_data')
        lib_stock_data = JSON_handler.load_file('lib_stock_data')
        back_up = {'members data': members_data, 'catalog data': catalog_data, 'lib stock data': lib_stock_data}
        date = dt.datetime.now().strftime('%d%m%Y-%H%M%S')
        file_name = f'back_up{date}'
        JSON_handler.save_file(back_up, file_name)
        time.sleep(1)


    def restore_back_up(file_name='backup_test.json'):
        back_up = JSON_handler.load_file(file_name)
        System.load_members_data(back_up['members data'])
        System.load_catalog_data(back_up['catalog data'])
        System.load_library_stock_data(back_up['lib stock data'])
        

    def load_catalog_data(dict=JSON_handler.load_file('catalog_data')):
        for book in dict['books']:
            book_object = Book(book['author'], book['country'], book['imageLink'], book['language'], 
            book['link'], book['pages'], book['title'], book['ISBN'], book['year'])
            if not Catalog.check_duplicate(book_object):
                Catalog.books.append(book_object)


    def save_catalog_data():
        JSON_handler.save_file(Catalog.to_dict(), 'catalog_data')


    def load_library_stock_data(dict=JSON_handler.load_file('lib_stock_data')):
        for book_item in dict['stock']:
            book = Book(book_item['book']['author'], book_item['book']['country'], book_item['book']['imageLink'],
            book_item['book']['language'], book_item['book']['link'], book_item['book']['pages'], book_item['book']['title'],
            book_item['book']['ISBN'], book_item['book']['year'])
            if not Catalog.check_duplicate(book):
                Catalog.books.append(book)
            Library_stock.stock.append(Book_item(book, book_item['id']))


    def save_library_stock_data():
        JSON_handler.save_file(Library_stock.to_dict(), 'lib_stock_data')


    def load_members_data(dict=JSON_handler.load_file('member_data')):
        for index, member in enumerate(dict['members']):
            Library_accounts.members.append(Member(member['number'], member['given_name'], member['surname'], 
            member['street_address'], member['zipcode'], member['city'], member['email_address'], 
            member['username'], member['password'], member['telephone_number']))
            for index2, loan_item in enumerate(member['loan_items']):
                Library_accounts.members[index].loan_items.append(Loan_item(Book_item(Book(loan_item['book_item']['book']['author'], loan_item['book_item']['book']['country'], 
                loan_item['book_item']['book']['imageLink'], loan_item['book_item']['book']['language'], loan_item['book_item']['book']['link'], 
                loan_item['book_item']['book']['pages'], loan_item['book_item']['book']['title'], loan_item['book_item']['book']['ISBN'], 
                loan_item['book_item']['book']['year']), loan_item['book_item']['id'])))
                Library_accounts.members[index].loan_items[index2].date_loaned = dt.datetime.strptime(loan_item['date_loaned'], '%d/%m/%Y').date()
                Library_accounts.members[index].loan_items[index2].return_due = dt.datetime.strptime(loan_item['return_due'], '%d/%m/%Y').date()


    def save_members_data():
        JSON_handler.save_file('member_data', Library_accounts.to_dict())
