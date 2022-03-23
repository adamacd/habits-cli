import sqlite3

conn = sqlite3.connect('habits.db')
cur = conn.cursor()

def view():
    cur.execute("SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable \
                WHERE active == 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewDaily():
    cur.execute(
                "SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable \
                WHERE periodicity == 'daily' AND active = 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewWeekly():
    cur.execute(
                "SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable \
                WHERE periodicity == 'weekly' AND active = 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewLifetime():
    cur.execute("SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable;")
    items = cur.fetchall()
    for element in items:
        print(element)

def streakBest():
    cur.execute(
        "SELECT description, streak from habitsTable \
        WHERE streak = (SELECT MAX(streak) FROM habitsTable)")
    items = cur.fetchone()
    for element in items:
        print(element, end= ' ')
    
def streak(rowid):
    cur.execute(
        "SELECT description, streak from habitsTable \
        WHERE rowid = (?)", (rowid))
    items = cur.fetchone()
    for element in items:
        print(element, end=' ')
