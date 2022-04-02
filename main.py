from Menu import Menu
from Catalog import Catalog
from Member import Member
from Library_admin import Library_admin


def Main() -> None:
    admin = Library_admin('admin', 'admin123')
    page_number = 0
    while(True):
        if page_number == 0:
            page_number = Menu.main_page()
        elif page_number == 1:
            page_number = Menu.members_login()
        elif page_number == 2:
            page_number = Menu.admin_login(admin)
        elif page_number == 99:
            return


if __name__ == '__main__':
    # Main()
    pass

# ------- Testing -------
Catalog.load_books()
Catalog.print_books()
