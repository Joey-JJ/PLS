from Library_accounts import Library_accounts


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
        print('Please enter your log in details for your members account...')
        username = input('Username: ')
        password = input('Password: ')
        print(username, password) # TODO: REMOVE
        return 0

    def admin_login(admin_account: object) -> int:
        print('Please enter your log in details for your members account...')
        logged_in = False
        while not logged_in:
            username = input('Username: ')
            password = input('Password: ')
            if username == admin_account.user_name and password == admin_account.password:
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
        user_input = input('What would you like to do?\n[1] See the current members\n[2] Add a new member\n[3] Edit a member [4] Log out and go back to the main menu\n')
        if user_input == '1':
            Library_accounts.list_members()
            return  4
        elif user_input == '2':
            Library_accounts.add_member()
            return 4
        elif user_input == '3':
            Library_accounts.edit_member('1')
            return 4
        elif user_input == '4':
            print('Logging out ...\n')
            return 0
