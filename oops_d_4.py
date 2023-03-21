class Member:
    "Create new member."
    def __init__(self,uname,fname):
        self.username = uname
        self.fullname = fname


new_guy = Member('Ravi','chikkala')

print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))