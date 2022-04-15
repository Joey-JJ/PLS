from Member import Member
import csv


class Library_accounts:
    members = []
    
    def to_dict():
        dict = {'members': Library_accounts.__dict__['members']}
        members = []
        for member in Library_accounts.__dict__['members']:
            members.append(member.to_dict())
        dict['members'] = members
        return dict
    

    def list_members() -> None:
        if len(Library_accounts.members) > 0:
            for member in Library_accounts.members:
                print(f'{member.number}. {member.given_name} {member.surname}')
            input('Press \'Enter\' to continue')
        else:
            print('There are no members at this point.')


    def search_member() -> object:
        member_number = input('Enter the number of the member: ')
        for member in Library_accounts.members:
            if member.number == str(member_number):
                return member
        return False


    def load_csv_members(filename: str):
        try:
            with open(filename) as file:
                csv_file = csv.reader(file, delimiter=';')
                for line in csv_file:
                    member_data = []
                    for value in line:
                        if value == 'Number':
                            break
                        member_data.append(value)
                    if len(member_data) > 0:
                        new_member = Member(member_data[0], member_data[1], member_data[2], member_data[3], member_data[4], member_data[5], member_data[6], member_data[7], member_data[8], member_data[9])
                        append = True
                        for mem in Library_accounts.members:
                            if mem.given_name == new_member.given_name and mem.surname == new_member.surname:
                                append = False
                        if append:
                            Library_accounts.members.append(new_member)
                print('Members saved\n')
                return 4
        except FileNotFoundError:
            print('File not found, please try again.')
            return 4


    def add_member() -> None:
        # TODO: SAVE CHANGES TO DATABASSE
        number = input("Enter the number: ")
        given_name = input("Enter the given name: ")
        surname = input("Enter the surname: ")
        street_address = input("Enter the street address: ")
        zipcode = input("Enter the zipcode: ")
        city = input("Enter the city: ")
        email_address = input("Enter the e-mail address: ")
        username = input("Enter the username (will be converted to lowercase): ").lower()
        password = input("Enter the password: ")
        telephone_number = input("Enter the telephone number: ")

        for member in Library_accounts.members:
            if member.number == number or member.given_name == given_name or member.username == username:
                print('There is already a user for this information in the system.')
                return

        new_member = Member(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)

        Library_accounts.members.append(new_member)
        print('Member added')


    def delete_member():
        # TODO: SAVE CHANGES TO DATABASSE
        del_number = input('Enter the number of the member you want to delete: ')
        for member in Library_accounts.members:
            if member.number == del_number:
                Library_accounts.members.remove(member)
                return 4
        print('Could not find member')
        return 4


    def edit_member() -> None:
        member = Library_accounts.search_member()
        if not member:
            print('Member was not found')
            return
        while True:
            to_edit = input(
                'What would you like to edit?\n' + \
                '[1] Number\n' + \
                '[2] Given name\n' + \
                '[3] Surname\n' + \
                '[4] Street address\n' + \
                '[5] Zipcode\n' + \
                '[6] City\n' + \
                '[7] E-mail address\n' + \
                '[8] Username\n' + \
                '[9] Password\n' + \
                '[10] Telephone number\n'
            )
            if to_edit == '1':
                new_num = input('Enter the number you would like to change it into: ')
                member.number = new_num
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '2':
                new_given_name = input('Enter the new given name: ')
                member.given_name = new_given_name
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '3':
                new_surname = input('Enter the new surname: ')
                member.surname = new_surname
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '4':
                new_street_address = input('Enter the new street address: ')
                member.street_address = new_street_address
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '5':
                new_zipcode = input('Enter the new street address: ')
                member.zipcode = new_zipcode
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '6':
                new_city = input('Enter the new city: ')
                member.city = new_city
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '7':
                new_email = input('Enter the new e-mail address: ')
                member.email = new_email
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '8':
                new_username = input('Enter the new username: ').lower()
                member.username = new_username
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '9':
                new_password = input('Enter the new password: ')
                member.password = new_password
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            elif to_edit == '10':
                new_phone = input('Enter the new telephone number: ')
                member.telephone_number = new_phone
                # TODO: SAVE CHANGES
                print('Change saved')
                return
            else:
                print('Please enter a valid option...')
