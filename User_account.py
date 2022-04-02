from datetime import datetime


class User_account(object):
    def __init__(self, user_name: str, password: str) -> None:
        self.user_name = user_name
        self.password = password
        self.date_created = datetime.today()