import sqlite3

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
'''
cur.execute(
    "SELECT * FROM habitsTable WHERE habit_id == ?",
    [id] #note, gotta be list, or else will be an error
    )

print(cur.fetchone())
'''

# Formatting results for analysis: show current, 
# show all, all daily, all weekly,
'''
cur.execute(
    "SELECT * FROM habitsTable"
)
items = cur.fetchall()
for element in items:
    print(str(element[0]) + " " + element[1] + "   " + element[2]) #ect.
'''

# 
datetime_last_completed = "2022-04-06, 315:343"
streak = 3
active = "yes"
habit_id = 3

cur.execute("""
            UPDATE habitsTable 
            SET 
            datetime_last_completed = ?,
            streak = ?,
            active = ?
            WHERE habit_id == ?
            """, ("2022-03-10, 09:53", 3, "Yes", 3)
            )

#check how to truncate tables here.
# ...
# ...

# submit changes
conn.commit()
conn.close()