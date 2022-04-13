import datetime


class Loan_item(object):
    def __init__(self, book_item):
        self.book_item = book_item
        self.date_loaned = datetime.date.today()
        self.return_due = self.date_loaned + datetime.timedelta(days=30)
        self.returned_on = None

    
    def to_dict(self) -> dict:
        dict = self.__dict__
        dict['book_item'] = self.book_item.to_dict()
        return dict


    def check_fine(self):
        if self.returned_on == None:
            print('The book has not been returned yet.')
            return
        if self.returned_on > self.return_due:
            return True
        else:
            return False
