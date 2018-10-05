#azrael - Jason Tung and Hasif Ahmed
#SoftDev1 pd8
#K17 -- Average
#2018-10-09
import copy
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
        reader = list(csv.DictReader(csvfile))
        headers = reader[0]
        command = "DROP TABLE IF EXISTS {0};".format(tablename)
        #print(command)
        c.execute(command)
        command = "CREATE TABLE IF NOT EXISTS {0}(".format(tablename)
        for keys in headers:
                command+= keys + " BLOB,"
        command = command[:-1]+ ");"
        #print(command)
        #print(command)
        c.execute(command)
        headerstr = ""
        for header in headers:
            headerstr+=header + ","
        headerstr=headerstr[:-1]
        for row in reader:
            #print(row)
            vals = ""
            for k,v in row.items():
                vals += "'{0}'".format(v) + ","
            vals = vals[:-1]
            command = "INSERT INTO {0}({1}) VALUES({2});".format(tablename,headerstr, vals)
            #print(command)
            c.execute(command)
        c.execute("SELECT * FROM {0};".format(tablename))
    # --------------------------------------------------------------------------------------------------

# ==========================================================
createtable('peeps.csv', 'peeps_info')

createtable('courses.csv', 'courses_info')



db.commit()  # save changes
db.close()  # close database


