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
'''
cur.execute (
    "INSERT INTO habitsTable VALUES (?,?,?,?, NULL, NULL, NULL)", 
    (id, periodicity, description, date)
)
print("successfully added")
'''

# get data from db
cur.execute(
    "SELECT * FROM habitsTable WHERE habit_id == ?",
    [id] #note, gotta be list, or else will be an error
    )

print(cur.fetchone())



# submit changes
conn.commit()
conn.close()