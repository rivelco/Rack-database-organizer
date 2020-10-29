import csv

def read_file(location):
    database = {}
    days = -1
    with open(location) as file:
        headers = ['Date', 'Day', 'Hour', 'Minute', 'Moves']
        reader = csv.DictReader(file, delimiter=' ', fieldnames=headers)
        for row in reader:
            day = int(row["Day"])
            hour = row["Hour"]
            minutes = row["Minute"]
            if len(hour) == 1:
                hour = "0" + hour
            if len(minutes) == 1:
                minutes = "0" + minutes
            time  = hour + minutes
            moves = int(row["Moves"])
            database[day] = database.get(day, {})
            if time in database[day]:
                tmstmp = time[:-2] + ":" + time[2:]
                print(" ++ Day " + str(day) + " with timestamp " + tmstmp + " is duplicated.")
                print("    Saving the first occurrence.")
            else:
                database[day][time] = moves
            if day > days:
                days = day
    return database, days
