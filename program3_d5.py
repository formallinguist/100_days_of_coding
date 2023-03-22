import datetime as dt

class Member:
    free_days = 0

    def __init__(self,username,fullname):
        self.date_joined = dt.date.today
        self.free_expires = dt.date.today() + dt.timedelta(Member.free_days)

    @classmethod
    def setfreedays(cls,days):
        cls.free_days = days

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

print(Member.currenttime())