def hello(fname, lname, datestring = " "):
    msg = "Hello " + fname + ' ' + lname
    if len(datestring) > 0:
        msg += "You mentioned " + datestring
    print(msg) 

hello("Alan ","Simpson ", "12/31/2109 ")
hello('Sammy ', 'Schmeedledorp ')