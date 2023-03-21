class Member:
    def __init__(self,uname,fname):
        self.uname = uname
        self.fname = fname


new_guy = Member("Ravi","Chikkala")

print(new_guy.uname)
print(new_guy.fname)

new_guy.uname = "Preethi"

print(new_guy.uname)
print(new_guy.fname)