import sqlite3
from datetime import datetime
from database import *

conn = sqlite3.connect('habits.db')
cur = conn.cursor()

def insert(periodicity, description, created):
    cur.execute (
    "INSERT INTO habitsTable VALUES (?,?,?, '', 0, 'Yes')", 
    (periodicity, description, created) )
    conn.commit()

def delete(rowid):
    cur.execute(
    "DELETE FROM habitsTable WHERE (?) == rowid", (rowid)
    )
    conn.commit()

def complete(rowid,completed):
    
    #cur.execute(
    #"UPDATE habitsTable SET active = 'No' WHERE rowid == (?)", (rowid)
    #)

    cur.execute("SELECT created, completed FROM habitsTable WHERE rowid == (?)", (rowid))
    dates = cur.fetchall()
    val1 = datetime.strptime(str(dates[0][0]), "%Y-%m-%d %X.%f")
    val2 = datetime.strptime(str(dates[0][1]), "%Y-%m-%d %X.%f")
    difference = val2 - val1
    difference2 = (difference.total_seconds() / 60**2)
    
    if difference2 > 24:
        print("you broke the streak, a day has passed.")
    else:
        print("the streak has not been broken.")

    cur.execute(
    "UPDATE habitsTable SET completed = (?) WHERE rowid == (?)", (completed, rowid)
    )
    
    cur.execute(
    "SELECT streak FROM habitsTable WHERE rowid == (?)", (rowid)
    )
    x = cur.fetchone()
    y = int(x[0] + 1)
    
    cur.execute(
    "UPDATE habitsTable SET streak = (?) WHERE rowid == (?)", (y, rowid)
    )
    
    conn.commit()

def clear():
    '''Runs a SQL command to TRUNCATE the table.'''
    cur.execute(
    "DELETE FROM habitsTable"
    )
    conn.commit()


