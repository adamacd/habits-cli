import sqlite3

conn = sqlite3.connect('habits.db')
cur = conn.cursor()

def view():
    cur.execute("SELECT rowid, * FROM habitsTable WHERE active == 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewDaily():
    cur.execute("SELECT rowid, * FROM habitsTable WHERE periodicity == 'daily';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewWeekly():
    cur.execute("SELECT rowid, * FROM habitsTable WHERE periodicity == 'weekly';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewLifetime():
    cur.execute("SELECT rowid, * FROM habitsTable;")
    items = cur.fetchall()
    for element in items:
        print(element)
