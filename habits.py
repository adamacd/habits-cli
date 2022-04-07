from database import *

class Habit:
    '''
    Creates a daily or weekly habit.
    '''
    def __init__(self, description, created):
        self.description = description
        self.created = created
        
    def createDaily(self):
        '''
        Insert a daily habit into the database.
        '''
        insert("daily", self.description, self.created, db_name())
        
    def createWeekly(self):
        '''
        Insert a weekly habit into the database.
        '''
        insert("weekly", self.description, self.created, db_name())
        
class HabitChangeState:
    '''
    Delete, complete habits
    '''
    def __init__(self, rowid):
        self.rowid = rowid
    
    def delete(self):
        '''
        Delete a habit from the database
        '''
        delete(self.rowid, db_name())

    def Completed(self, date_completed):
        '''
        Attempt to mark a habit as complete, and increment the streak.
        '''
        complete(self.rowid, date_completed, db_name())
