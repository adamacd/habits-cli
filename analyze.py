from database import view_rows

def view():
    x = view_rows()
    xcopy = x.copy()
    print(x[0][-3:])

def viewDaily():
    pass

def viewWeekly():
    pass

def viewLifetime():
    pass

view()