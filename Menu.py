from Catalog import Catalog
from Library_accounts import Library_accounts
from Library_admin import Library_admin
from Library_stock import Library_stock
from Library_system import System


class Menu:
    """Static class for the menu pages"""
    def main_page() -> int:
        while True:
            print('Welcome to the Public Library System!\n[1] Log in (Members)\n[2] Log in (Admin)\n[3] Quit the application\n')
            user_input = input('Please enter your selection: ')
            if user_input == '1':
                return 1
            elif user_input == '2':
                return 2
            elif user_input == '3':
                return 99
            else:
                print('Please enter a valid option\n')

    def members_login() -> int:
        while True:
            print('Please enter your log in details for your members account...')
            username = input('Username: ')
            password = input('Password: ')
            for member in Library_accounts.members:
                if member.username == username and member.password == password:
                    print(f'Logged in as {member.username}')
                    return (3, member)
            print('\nInvalid username/password, please try again. To quit the application, enter \'quit\', else press enter')
            quit = input()
            if quit == 'quit':
                return (0, None)
    

    def member_section(member):
        options = 'What would you like to do?\n[1] Check the catalog\n[2] Search a book in the catalog\n[3] See the list of book items in the library\n[4] Search a book item\n[5] Loan a book item\n[6] Return a book item\n[7] Return to the main menu\n'
        while True:
            user_input = input(options)
            if user_input == '1':
                Catalog.list_books()
            elif user_input == '2':
                Catalog.search()
            elif user_input == '3':
                Library_stock.list_stock()
            elif user_input == '4':
                Library_stock.search_book_item()
            elif user_input == '5':
                member.loan_book_item()
                System.save_all_data()
            elif user_input == '6':
                member.return_book_items()
                System.save_all_data()
            elif user_input == '7':
                return 0
            return 3


    def admin_login(admin_account: object) -> int:
        logged_in = False
        while not logged_in:
            print('Please enter your log in details for your admin account...')
            username = input('Username: ')
            password = input('Password: ')
            if username == admin_account.username and password == admin_account.password:
                print('You are now logged in as admin\n')
                logged_in = True
                return 4
            else:
                print('\nInvalid username/password, please try again. To quit the application, enter \'quit\', else press enter')
                quit = input()
                if quit == 'quit':
                    break
        return 0

    def admin_section() -> int:
        options = "What would you like to do?\n[1] See the current members\n\
[2] Add a new member\n[3] Edit a member\n\
[4] Import members from a CSV file\n\
[5] Delete a members account\n[6] Check the status of book items currently loaned by members\n\
[7] Check the catalog\n[8] Add a book to the catalog\n[9] Edit a book from the catalog\n\
[10] Delete a book from the catalog\n[11] Search a book in the catalog\n[12] Add a list of books (using a JSON file)\n\
[13] List book items\n[14] Add a book item\n[15] Edit a book item\n[16] Delete a book item\n\
[17] Search a book item\n[18] Lend a book item to a member\n[19] Make a back-up of the system\n\
[20] Restore a back-up of the system\n[21] Log out and go back to the main menu\n"
        while True:
            user_input = input(options)
            if user_input == '1':
                Library_accounts.list_members()
                return  4
            elif user_input == '2':
                Library_accounts.add_member()
                System.save_all_data()
                return 4
            elif user_input == '3':
                Library_accounts.edit_member()
                System.save_all_data()
                return 4
            elif user_input == '4':
                filename = input('Enter the full name of the CSV file: ')
                Library_accounts.load_csv_members(filename)
                System.save_all_data()
                return 4
            elif user_input == '5':
                Library_accounts.delete_member()
                System.save_all_data()
                return 4
            elif user_input == '6':
                Library_admin.check_loan_status()
                return 4
            elif user_input == '7':
                Catalog.list_books()
                return 4
            elif user_input == '8':
                Catalog.add_book()
                System.save_all_data()
                return 4
            elif user_input == '9':
                Catalog.edit_book()
                System.save_all_data()
                return 4
            elif user_input == '10':
                Catalog.delete_book()
                System.save_all_data()
                return 4
            elif user_input == '11':
                Catalog.search()
                System.save_all_data()
                return 4
            elif user_input == '12':
                file_name = input('Please enter the name of the JSON file: ')
                Catalog.load_books(file_name)
                System.save_all_data()
                return 4
            elif user_input == '13':
                Library_stock.list_stock()
                return 4
            elif user_input == '14':
                Library_stock.add_book_item()
                System.save_all_data()
                return 4
            elif user_input == '15':
                Library_stock.edit_book_item_id()
                System.save_all_data()
                return 4
            elif user_input == '16':
                Library_stock.delete_book_item()
                System.save_all_data()
                return 4
            elif user_input == '17':
                Library_stock.search_book_item()
                System.save_all_data()
                return 4
            elif user_input == '18':
                Library_admin.lend_to_member()
                System.save_all_data()
                return 4
            elif user_input == '19':
                System.make_back_up()
                print('Made the back-up')
                return 4
            elif user_input == '20':
                file_name = input('Enter the name of the back-up file: ')
                try:
                    System.restore_back_up(file_name)
                    System.save_all_data()
                except:
                    print('File not found, try again.')
                return 4
            elif user_input == '21':
                print('Logging out ...\n')
                return 0
            else:
                print('Please enter a valid number.')
