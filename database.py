import sqlite3
''' SQL TABLE COLUMNS
habit_id
periodicity/TEXT
description/TEXT
datetime_created/TEXT
datetime_last_completed/TEXT nullable
streak/INTEGER nullable
active/TEXT nullable
'''
# connect to db
conn = sqlite3.connect('habits.db')

# create a cursor
cur = conn.cursor()

# insert one record into table by variable ?
id = 4
periodicity = 'weekly'
description = 'new format testin'
date = '2022-03-07, 15:13'
cur.execute (
    "INSERT INTO habitsTable VALUES (?,?,?,?, NULL, NULL, NULL)", 
    (id, periodicity, description, date)
)
print("successfully added")

# submit changes
conn.commit()
conn.close()