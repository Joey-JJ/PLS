from Library_accounts import Library_accounts
from Menu import Menu
from Catalog import Catalog
from Member import Member
from Library_admin import Library_admin


def Main() -> None:
    admin = Library_admin(0, "admin", "", "", "", "", "admin@PLS.com", "admin", "admin123", 0)
    page_number = 0
    while(True):
        if page_number == 0:
            page_number = Menu.main_page()
        elif page_number == 1:
            page_number = Menu.members_login()
        elif page_number == 2:
            page_number = Menu.admin_login(admin)
        elif page_number == 4:
            page_number = Menu.admin_section()
        elif page_number == 99:
            return


if __name__ == '__main__':
    # Library_accounts.load_csv_members('Members.csv')
    # Library_accounts.list_members()
    pass