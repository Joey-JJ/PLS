from Book import Book
from Book_item import Book_item
from JSON import JSON_handler
from Library_accounts import Library_accounts
from Library_stock import Library_stock
from Loan_item import Loan_item
from Menu import Menu
from Member import Member
from Library_admin import Library_admin
from Catalog import Catalog
import datetime as dt


def load_library_stock_data():
    dict = JSON_handler.load_file('lib_stock_data')
    for book_item in dict['stock']:
        book = Book(book_item['book']['author'], book_item['book']['country'], book_item['book']['imageLink'],
        book_item['book']['language'], book_item['book']['link'], book_item['book']['pages'], book_item['book']['title'],
        book_item['book']['ISBN'], book_item['book']['year'])
        Library_stock.stock.append(Book_item(book, book_item['id']))


def save_library_stock_data():
    JSON_handler.save_file(Library_stock.to_dict(), 'lib_stock_data')


def load_members_data():
    dict = JSON_handler.load_file('member_data')
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



def Main() -> None:
    admin = Library_admin(0, "admin", "", "", "", "", "admin@PLS.com", "admin", "admin123", 0)
    member = Member('1', 'test', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'member', 'member123', 'xxx') # TODO: REMOVE
    Library_accounts.members.append(member)

    page_number = 0

    while(True):
        if page_number == 0:
            page_number = Menu.main_page()
        elif page_number == 1:
            pagenumber_and_member = Menu.members_login()
            page_number = pagenumber_and_member[0] 
        elif page_number == 2:
            page_number = Menu.admin_login(admin)
        elif page_number == 3:
            page_number = Menu.member_section(pagenumber_and_member[1])
        elif page_number == 4:
            page_number = Menu.admin_section()
        elif page_number == 99:
            return

# if __name__ == '__main__':
#     Main()

# BACKUP: 
# Member data:                 Library accounts -> Member -> Loan item -> Book item -> Book
# TODO: Library stock data:     Library stock -> Book item -> Book
# TODO: Catalog data:           Catalog -> Book
