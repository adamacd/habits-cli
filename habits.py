from datetime import datetime
from database import *

class Habit:
    
    def __init__(self, description, created):
        self.description = description
        self.created = created
        
    def createDaily(self):
        insert("daily", self.description, self.created)
        
    def createWeekly(self):
        insert("weekly", self.description, self.created)


