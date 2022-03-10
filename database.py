import sqlite3


sql_tablE_columns = ["habit_id", "periodicity/TEXT", "description/TEXT",
                     "datetime_created/TEXT", "datetime_last_completed/TEXT nullable",
                     "streak/INTEGER nullable", "active/TEXT nullable"
                     ]
def columnNames(list):
    for element in list:
        print(element + "\n")
columnNames(sql_tablE_columns)


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

cur.execute("""
            UPDATE habitsTable 
            SET datetime_last_completed = '2022-03-08, 11:42', 
            streak = 1, 
            active = 'Yes'
            WHERE habit_id == 3
            """
            )

# submit changes
conn.commit()
conn.close()