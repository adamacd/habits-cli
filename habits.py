from database import *

class Habit:
    
    def __init__(self, description, created):
        self.description = description
        self.created = created
        
    def createDaily(self):
        insert("daily", self.description, self.created)
        
    def createWeekly(self):
        insert("weekly", self.description, self.created)
        
class HabitChangeState:
    
    def __init__(self, rowid):
        self.rowid = rowid
        
    def delete(self):
        delete(self.rowid)

    def clear(self):
        clear()

    def Completed(self, date_completed):
        complete(self.rowid, date_completed)

