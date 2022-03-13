import sqlite3

conn = sqlite3.connect('habits.db')
cur = conn.cursor()

def insert(periodicity, description, created):
    cur.execute (
    "INSERT INTO habitsTable VALUES (?,?,?, NULL, NULL, 'Yes')", 
    (periodicity, description, created) )
    conn.commit()

def delete():
    pass

def complete():
    pass

def clear():
    pass

def view_rows():
    cur.execute(
    "SELECT rowid, * FROM habitsTable"
    )
    items = cur.fetchall()
    list = []
    for element in items:
        list.append( str(element[0]) + " " + element[1] + "  " + element[2] + "  " + element[3][0:16] + "  " + str(element[4]) + "  " + str(element[5]) + "  " + str(element[6]))
    return list
