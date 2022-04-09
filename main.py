from Library_accounts import Library_accounts
from Menu import Menu
from Member import Member
from Library_admin import Library_admin
from Catalog import Catalog


def Main() -> None:
    admin = Library_admin(0, "admin", "", "", "", "", "admin@PLS.com", "admin", "admin123", 0)
    member = Member('1', 'Joey', 'vd Valk', 'xxx', 'xxx', 'xxx', 'xxx', 'member', 'member123', 'xxx') # TODO: REMOVE
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

if __name__ == '__main__':
    # Main()
    pass
