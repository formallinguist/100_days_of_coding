import datetime as dt

class Member:
    def __init__(self,username,fullname):
        self.username = username
        self.fullname = fullname

        self.date_joined = dt.date.today()

        self.is_active = True

    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"

    def activate(self,yesno):
        self.is_activate = yesno

new_guy = Member('Rombo','Rocco Moe')

print(new_guy.is_active)

new_guy.is_active = False

print(new_guy.is_active)