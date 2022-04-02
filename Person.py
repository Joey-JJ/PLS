from ast import Pass
from sympy import N


class Person(object):
    # Number;GivenName;Surname;StreetAddress;ZipCode;City;EmailAddress;Username;Password;TelephoneNumber
    def __init__(self, Number, GivenName, Surname, StreetAddress, Zipcode, City, EmailAddress, Username, Password, TelephoneNumber) -> None:
        self.number = Number
        self.given_name = GivenName
        self.surname = Surname
        self.street_address = StreetAddress
        self.zipcode = Zipcode
        self.city = City
        self.email_address = EmailAddress
        self.user_name = Username
        self.password = Password
        self.telephone_number = TelephoneNumber
        