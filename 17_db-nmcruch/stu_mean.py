#azrael - Jason Tung and Hasif Ahmed
#SoftDev1 pd8
#K17 -- Average
#2018-10-09
import copy
import sqlite3  # enable control of an sqlite database
import csv  # facilitates CSV I/O
import os

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
        command = "CREATE TABLE IF NOT EXISTS {0}".format(tablename)
        command += "("
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
        #c.execute("SELECT * FROM {0};".format(tablename))
    # --------------------------------------------------------------------------------------------------

# ==========================================================
createtable("peeps.csv", 'peeps_info')
createtable('courses.csv', 'courses_info')

db.commit()  # save changes
db.close()  # close database


db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops

def createAvgtbl():
    peeps_dict ={}

    info = c.execute(
        "SELECT name, peeps_info.id, mark FROM peeps_info, courses_info WHERE peeps_info.id = courses_info.id;")
    for list in info: #iterate through the list of names
        name = str(list[0])
        id = int(list[1])
        grade = float(list[2])
        if name not in peeps_dict:
            s_dict = {}
            s_dict["id"] = id
            s_dict["tot_grades"] = grade
            s_dict["classes"] = 1
            peeps_dict[name] = s_dict
        else:
            peeps_dict[name]["tot_grades"] += grade
            peeps_dict[name]["classes"] += 1
        peeps_dict[name]["avg"] = peeps_dict[name]["tot_grades"]/s_dict["classes"]
    command = "DROP TABLE IF EXISTS {0};".format("peeps_avg")
    c.execute(command)
    c.execute("CREATE TABLE IF NOT EXISTS peeps_avg(id INTEGER, name TEXT, average DECIMAL);") #create peeps_avg
    for k,v in peeps_dict.items(): #iterate through dictrionary with items() so u can access key and value
        name = k;
        id = v["id"]
        avg = v["avg"]
        command = "INSERT INTO peeps_avg VALUES({id},'{name}',{avg});".format(id = id, name = name, avg = avg) #insert them
        #rprint(command)
        c.execute(command) #execute command 

def printTable(name):
    c.execute('SELECT * FROM {name}'.format(name=name))
    print(c.fetchall())

def addStuff(code, id, mark):
    c.execute("INSERT INTO courses_info VALUES('{code}','{id}','{mark}')".format(code = code,id = id,mark = mark))
    

createAvgtbl()
print("peeps_avg:")
printTable("peeps_avg")
print("courses after adding 1000 to tiesto:")
addStuff("bicycle eating", "5", "1000")
createAvgtbl()
printTable("courses_info")
printTable("peeps_avg")
db.commit()  # save changes
db.close()  # close database


