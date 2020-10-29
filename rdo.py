import sys
import csv
import os
from RDO_files import greetings as g
from RDO_files import read_file as rf
from RDO_files import save_table as st

def main(locations):
    for location in locations:
        print("\nProcessing " + location)
        if os.path.isfile("./" + location):
            database, days = rf.read_file(location)
            output_location = location[:-4] + "_table.csv"
            print("Saving " + location + " table as " + output_location)
            st.save_table(output_location, database, days)
        else:
            print(" >> File " + location + " not found.")

if __name__ == "__main__":
    g.greetings()

    locations = []
    print("Looking for input data...")
    if os.path.isfile("./files_rdo.txt"):
        with open("files_rdo.txt") as file:
            reader = csv.reader(file)
            for row in reader:
                for element in row:
                    locations.append(element)
    elif len(sys.argv) > 1:
        locations = sys.argv[1:]
    else:
        print("The program didn't receive any input data.")
        print("Nothing was changed.")
        exit()

    print("Done.")
    main(locations)
    print("\nFinished.")
    os.system("pause")
