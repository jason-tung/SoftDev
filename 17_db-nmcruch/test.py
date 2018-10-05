import csv

readfile = csv.DictReader(open("courses.csv"))
print(readfile)
for x in readfile:
    print(x)