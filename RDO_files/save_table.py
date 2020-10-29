import csv
import pathlib

def save_table(location, database, days):
    filepath = pathlib.Path(location)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open(mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = ['Timestamp']
        for day in range(1, days+1):
            headers.append("M" + str(day))
        writer.writerow(headers)
        for day in range(1, days+1):
            if not day in database:
                print(" -- Entire day " + str(day) + " is missing.")
                print("    Filling with hyphens ( - ).")
        for i in range(96):             
            new_row = []
            minutes = str((i*15)%60)
            hour = str((i*15)//60)
            if len(hour) == 1:
                hour = "0" + hour
            if len(minutes) == 1:
                minutes = "0" + minutes
            time = hour + ":" + minutes
            new_row.append(time)
            for day in range(1, days+1):
                if not day in database:
                    new_row.append("-")
                elif hour+minutes in database[day]:
                    new_row.append(database[day][hour+minutes])
                else:
                    print(" -- Day " + str(day) + " with timestamp " + time + " is missing.")
                    print("    Hyphen added in that place.")
                    new_row.append("-")
            writer.writerow(new_row)
