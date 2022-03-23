import sqlite3
from datetime import datetime
from database import *

conn = sqlite3.connect('habits.db')
cur = conn.cursor()

def insert(periodicity, description, created):
    cur.execute (
    "INSERT INTO habitsTable VALUES (?,?,?, '', 0, 'Yes')", 
    (periodicity, description, created))
    conn.commit()

def delete(rowid):
    cur.execute(
    "DELETE FROM habitsTable WHERE (?) == rowid", (rowid))
    conn.commit()

def complete(rowid,completed):
    
    cur.execute("SELECT created FROM habitsTable WHERE rowid == (?)", (rowid))
    dates = cur.fetchall()
    val1 = datetime.strptime(str(dates[0][0]), "%Y-%m-%d %X.%f")
    val2 = completed
    difference = val2 - val1
    hours = (difference.total_seconds() / 60**2)
    
    cur.execute("SELECT periodicity FROM habitsTable WHERE rowid == (?)", (rowid))
    periodicity = cur.fetchall()[0][0]
    
    if ((periodicity == 'daily') and (hours > 24)) or ((periodicity == 'weekly') and (hours > 168)):
        
        cur.execute(
        "UPDATE habitsTable SET active = 'No' WHERE rowid == (?)", (rowid))
        conn.commit()
        print("You did not complete the habit in time; the streak is broken.")

    else:
        
        cur.execute(
        "UPDATE habitsTable SET completed = (?) WHERE rowid == (?)", (completed, rowid))
        
        cur.execute(
        "UPDATE habitsTable SET created = (?) WHERE rowid == (?)", (completed, rowid))
        
        cur.execute(
        "SELECT streak FROM habitsTable WHERE rowid == (?)", (rowid))
        x = cur.fetchone()
        y = int(x[0] + 1)
        
        cur.execute(
        "UPDATE habitsTable SET streak = (?) WHERE rowid == (?)", (y, rowid)
        )
        conn.commit()
        print("Success. +1 added to your habit streak.")
        
def clear():
    '''Runs a SQL command to TRUNCATE the table.'''
    cur.execute(
    "DELETE FROM habitsTable"
    )
    conn.commit()
    