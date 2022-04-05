import sqlite3
from datetime import datetime
from database import *

def db_name(name='habits.db'):
    conn = sqlite3.connect(name)
    return conn

def make_db(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS habitsTable ( 
        periodicity TEXT NOT NULL, 
        description TEXT NOT NULL, 
        created TEXT NOT NULL, 
        completed TEXT, 
        streak INTEGER, 
        active TEXT);
        ''')

def insert(periodicity, description, created, conn):
    '''
    Insert a row into the database.
    :param periodicity: 'daily' or 'weekly'
    :param description: user defined habit
    :param created: date of habit creation
    '''
    cur = conn.cursor()
    cur.execute (
    "INSERT INTO habitsTable VALUES (?,?,?, '', 0, 'Yes')", 
    (periodicity, description, created))
    conn.commit()

def delete(rowid, conn):
    '''
    Delete a row from the database.
    :param rowid: the row id corresponding to a row to be deleted
    '''
    cur = conn.cursor()
    cur.execute(
    "DELETE FROM habitsTable WHERE (?) == rowid", (rowid))
    conn.commit()

def complete(rowid,completed, conn):
    '''
    Adds 1 to the streak counter in database if complete, removes habit if habit is incomplete.
    :param rowid: rowid from SQLite
    :param completed: date the user runs the complete function in main.py
    '''
    
    #Convert the string in the database to a python datetime object to compare times.
    #Check if 24, or 168 hours has passed.
    #Break the daily, or weekly streak if the user tries to check in too late.
    cur = conn.cursor()
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
        
def clear(conn):
    '''Runs a SQL command to TRUNCATE the table.'''
    cur = conn.cursor()
    cur.execute(
    "DELETE FROM habitsTable"
    )
    conn.commit()