def sorter(*args):
    """ Pass in any number of arguments seperated by commas
         Inside the function, they treated as a tuple named args """
    newlist = list(args)
    newlist.sort()
    print(newlist)

sorter(1, 0.001, 100000, -900, 2)