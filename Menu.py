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
            else:
                print('\nInvalid username/password, please try again. To quit the application, enter \'quit\', else press enter')
                quit = input()
                if quit == 'quit':
                    break
        return 0