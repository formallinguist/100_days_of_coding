import datetime as dt

class Member:
    def __init__(self,username,fullname):
        self.username = username
        self.fullname = fullname
        self.date_joined = dt.date.today()
        self.is_activate = True

    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"

new_guy = Member("Ravi","Kiran")

print(new_guy.show_datejoined())