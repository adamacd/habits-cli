import sqlite3

conn = sqlite3.connect('habits.db')
cur = conn.cursor()

def view():
    '''
    SQL Query to retrieve active habits. Python print for clarity for the user.
    '''
    cur.execute("SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable \
                WHERE active == 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewDaily():
    '''
    SQL Query to view daily habits.
    '''
    cur.execute("SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable \
                WHERE periodicity == 'daily' AND active = 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewWeekly():
    '''
    SQL Query to view weekly habits.
    '''
    cur.execute("SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable \
                WHERE periodicity == 'weekly' AND active = 'Yes';")
    items = cur.fetchall()
    for element in items:
        print(element)

def viewLifetime():
    '''
    SQL Query to view all habits, including expired.
    '''
    cur.execute("SELECT rowid, periodicity, description, substr(created,0,17) AS created FROM habitsTable;")
    items = cur.fetchall()
    for element in items:
        print(element)

def streakBest():
    '''
    SQL Query to view the row with the MAX streak.
    '''
    cur.execute(
        "SELECT description, streak from habitsTable \
        WHERE streak = (SELECT MAX(streak) FROM habitsTable)")
    items = cur.fetchone()
    for element in items:
        print(element, end= ' ')
    
def streak(rowid):
    '''
    Print the streak value according to the rowid given by user.
    :param rowid: rowid given by user, that corresponds to a rowid in the database.
    '''
    try:
        cur.execute(
            "SELECT description, streak from habitsTable \
            WHERE rowid = (?)", (rowid))
        items = cur.fetchone()
        for element in items:
            print(element, end=' ')
    except:
        print("That habit ID does not exist.")