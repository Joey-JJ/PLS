from Menu import Menu
from Members_account import Members_account
from Admin_account import Admin_account


def Main() -> None:
    # admin = Admin_account('admin', 'admin123')
    page_number = 0
    while(True):
        if page_number == 0:
            page_number = Menu.main_page()
        elif page_number == 1:
            page_number = Menu.members_login()
        elif page_number == 2:
            page_number = Menu.admin_login()
        elif page_number == 99:
            return


if __name__ == '__main__':
    Main()