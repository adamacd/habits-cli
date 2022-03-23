from datetime import datetime

val1 = datetime.now()

val2 = datetime(2022,3,24,11,17)

fag = str(val1)


print(val1)
print(val2)

#difference in hours
difference = val1 - val2
print(difference.total_seconds() / 60**2)