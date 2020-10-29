# Rack database organizer

This program analyzes and organizes the activity data file of a rack that measures the locomotor activity of experimental animals. The program generates a table with the locomotor quantification of an experimental animal in a given day and time.

> This is a very specific program for a very specific problem.

## How to prepare my computer to run this program

- Install python 3 from https://www.python.org/downloads/
- Make sure that you check the `Add to PATH` box at the bottom of the installation window.
- Open your favorite terminal or command interpreter:
  - If you're using Windows, type `cmd` in the search bar of the Start Menu (the one that has the Windows Logo)
  - If you're using macOS, click the Launchpad icon in the Dock, type `Terminal` in the search field, then click Terminal.
- Make sure you have installed python correctly by typing in the terminal:
  - `python --version` then hit the `Intro` key, if you're using Windows
  - `python3 --version` then hit the `Intro` key, if you're using macOS
- The terminal must show something like `Python 3.X.X`. If this is not your case try reinstalling Python, make sure to check the `Add to PATH` box.

## How to run this program

- Download this program by going to https://github.com/rivelco/Rack-database-organizer/releases
- You'll need to have the file `rdo.py` and the folder `RDO_files` together (in the same folder) all the time.
- You can specify the files you want to analyze by creating a text file called `files_rdo.txt`, this file must be in the same folder of the file `rdo.py`. Inside this file you must specify the name of the files you want to analyze. This names may be one name on each line or all the names separated by commas in the same line.
- I recommend putting all the files to analyze inside of a specific folder, called `data`, for example.
- If inside this `data` folder you have your files to analyze like `R2H1S3.txt`, `R1H2S4.txt` and `R3H1S2.txt`, your `files_rdo.py` will look like:

```
data/R2H1S3.txt
data/R1H2S4.txt
data/R3H1S2.txt
```

- At the end, you'll have a folder tree like this:

```
data/
|-- R2H1S3.txt
|-- R1H2S4.txt
|__ R3H1S2.txt
RDO_files/
|-- greetings.py
|-- read_file.py
|__ save_table.py
files_rdo.txt
rdo.py
```

### Running the program

- Now just double click the `rdo.py` file.

## Output of this program

- The program will generate one output file for each input file with the same name except for the end. The output file ends with `_table.csv` so if you analyze the file `R2H1S3.txt` the program will generate a file called `R2H1S3_table.csv` in the same folder where `R2H1S3.txt` is.
- The program will also show in the console some messages:
  - Name and version of the program
  - Link to the repository of the program
  - A `Looking for input data...` message. If the program don't find the one of the files that you want to analyze then it'll show an error message.
  - A line for each file to analyze, indicating the status of the analysis.
  - The program may show some error messages like:
    - `Day X with timestamp HH:MM is duplicated` when there are two registers for the same day and time in one file. In this case the program will save only the first occurrence.
    - `Day X with timestamp HH:MM is missing` when there's not a register for a specific time and day. In this case the program will save a `-` for that day and time.
    - `Entire day X is missing.` when an entire day is missing in the file to analyze. In this case the program will save a `-` for all the values of that day.
  - A `Finished` message when the program ends.

### Structure of the output files

- This program will generate a table, in the headers will be `Timestamp` and a `M1`, `M2` ... `MN`. One `MX` for each day in the file analyzed.
- In the first column, the `Timestamp` column, will be all the hours of one day in blocks of 15 minutes. It'll start with `00:00`, `00:15`, `00:30` ... `23:45`.
- In the other columns will be an integer (or a hyphen if the program found a mistake) indicating the quantification of the movement for a given day at an specific time.
- The format of each output file will `.csv`

## Structure of the expected  file to analyze

- It's expected that all the files to analyze has the same structure.
- The name and extension of the file doesn't matter as long as they are in plain text, like `.txt`, `.csv`, `.md`, etc. Excel files `.xlsx` or PDF files `.pdf` are not supported.
- The files shouldn't have any header.
- Each line in the file must follow the same structure `date day hour minute moves`.
- So a line with the content `20200220 1 2 15 68` will be interpreted as: *The day 20 of February 2020, is considered as the day one of register, and at the time 02:15 the animal recorded a movement of 68*.

## How to cite this program

If you find this program useful in your research, please cite this program like this:

> Velázquez R. (2020). Rack database organizer (v1) [Computer software]. Retrieved from https://github.com/rivelco/Rack-database-organizer
