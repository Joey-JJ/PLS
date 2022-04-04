from Member import Member


class Library_accounts:
    members = []
    
    def list_members() -> None:
        if len(Library_accounts.members) > 0:
            print('\n')
            for member in Library_accounts.members:
                print(f'{member.number}. {member.given_name} {member.surname}')
            print('\n')
        else:
            print('There are no members at this point.')

    def search_member(member_number: int) -> object:
        for member in Library_accounts.members:
            if member.number == member_number:
                return member
        return False
        
    def add_member() -> None:
        # TODO: SAVE CHANGES TO DATABASSE
        number = int(input("Enter the number: "))
        given_name = input("Enter the given name: ")
        surname = input("Enter the surname: ")
        street_address = input("Enter the street address: ")
        zipcode = input("Enter the zipcode: ")
        city = input("Enter the city: ")
        email_address = input("Enter the e-mail address: ")
        username = input("Enter the username (will be converted to lowercase): ").lower()
        password = input("Enter the password: ")
        telephone_number = input("Enter the telephone number: ")

        new_member = Member(number, given_name, surname, street_address, zipcode, city, email_address, username, password, telephone_number)

        Library_accounts.members.append(new_member)
        print('Member added')
    
    def edit_member(member_number: int) -> None:
        member = Library_accounts.search_member(member_number)
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


    
