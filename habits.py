import time

''' SQL TABLE COLUMNS
habit_id
periodicity/TEXT
description/TEXT
datetime_created/TEXT
datetime_last_completed/TEXT nullable
streak/INTEGER nullable
active/TEXT nullable
'''

class Habit:
    
    def __init__(self, periodicity, description, datetime_created):
        self.periodicity = periodicity
        self.description = description
        self.datetime_created = datetime_created
        
    def createDaily(self):
        pass
        
    def createWeekly(self):
        pass

x = Habit("daily", "read news online", "2022-03-06, 15:30")

