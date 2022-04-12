from Library_accounts import Library_accounts
from Person import Person


class Library_admin(Person):
    def __init__(self, number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number) -> None:
        super().__init__(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)

    def check_loan_status():
        for member in Library_accounts.members:
            print(f'{member.number}. {member.given_name} {member.surname}: {member.loan_items}')

    
    def lend_to_member():
        if len(Library_accounts.members) == 0:
            print('There are no members currently')
            return
        for member in Library_accounts.members:
                print(f'{member.number}. {member.given_name} {member.surname}')
        member_number = input('Enter the number of the member you want to lend a book to: ')
        member_to_lend_to = None
        for member in Library_accounts.members:
            if member.number == member_number:
                member_to_lend_to = member
        if member_to_lend_to != None:
            member_to_lend_to.loan_book_item()
