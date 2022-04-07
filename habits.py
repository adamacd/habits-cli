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
    Delete, complete, or clear habits.
    '''
    def __init__(self, rowid):
        self.rowid = rowid
    
    def delete(self):
        delete(self.rowid, db_name())

    def Completed(self, date_completed):
        complete(self.rowid, date_completed, db_name())
