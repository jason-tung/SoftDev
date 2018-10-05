#azrael - Jason Tung and Hasif Ahmed
#SoftDev1 pd8
#K17 -- Average
#2018-10-09

import sqlite3  # enable control of an sqlite database
import csv  # facilitates CSV I/O

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops


# ==========================================================
# INSERT YOUR POPULATE CODE IN THIS ZONE

def createtable(filename, tablename):
    # creating the initial exec statement: declaring table name, columns and column definitions -------

    # --------------------------------------------------------------------------------------------------

    # executing row statements--------------------------------------------------------------------------
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        command = "DROP TABLE IF EXISTS {0};".format(tablename)
        c.execute(command)
        command = "CREATE TABLE IF NOT EXISTS {0}(".format(tablename)
        for row in reader:
            for keys in row:
                command+= keys + " BLOB,"
        command = command[:-1]+ ");"
        c.execute(command)
        for row in reader:
            for k,v in row:
                command = "INSERT INTO {0} VALUES {1};".format(k, v)
                c.execute(command)
    # --------------------------------------------------------------------------------------------------

# ==========================================================
createtable('peeps.csv', 'peeps_info')

createtable('courses.csv', 'courses_info')



db.commit()  # save changes
db.close()  # close database


