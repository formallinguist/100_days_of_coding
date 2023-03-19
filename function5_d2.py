def hello(fname, lname, datestring):
    """ A doc string describing the function"""
    msg = "Hello " + fname +" "+ lname
    msg += "you mentioned" + datestring
    print(msg)

hello(datestring="12/31/2019",lname="Simpson", fname="Alan")

app_date = "12/31/2019"
kname = "Ravi"
mname = "Teja"

hello(datestring = app_date, fname = kname, lname = mname)