# azrael - Jason Tung and Simon Tsui (updated on 09/24/18 to use for 10_occupy_flask)
# SoftDev1 pd8
# K10 -- StI/O: Divine your Destiny!
# 2018-09-13
import csv
import random

def convert(filename):
    '''converts a two column csv file with table headers and footers into a key value pair dictionary'''
    #open file and parse it into a generator using csv reader
    #convert the generator into a list exluding the job and percentage table headers and footers
    #read values two at a time as tuples and use those to create a key value pair
    f = {occupationName:[float(percentage),linkToPage] for occupationName,percentage,linkToPage in list(csv.reader(open(filename)))[1:-1]}
    return f

def pickRandom(f):
    '''takes a dictionary of key value pairs and returns a random key using the values as the percent chance of selecting the corresponding key'''
    #pick a number, any number (as long as it's an element of [0,99.8))
    rand = random.uniform(0, 99.8)
    #go through key value pairs in f
    for occupationName,listOfPercentsAndLinks in f.items():
        percentageOfCurrentOcc = listOfPercentsAndLinks[0]
        rand -= percentageOfCurrentOcc
        #when the cumulative total is greater than the random value, return that key
        if rand <= 0:
            return occupationName
    print("uh oh... something has gone awry!")

def main():
    dictionaryFromCSV = convert("occupations.csv")
    print("appropriate dictionary: ", dictionaryFromCSV)
    # print(reduce(lambda x,y: x+y, ([v for k,v in f.items()])))
    print("weighted random pick: ", pickRandom(dictionaryFromCSV))
    print("--testing--")
    test()

def test():
    dictFromCSV = convert("occupations.csv")
    newDict = {occupation:0 for occupation in dictFromCSV}
    for x in range(10000):
        newDict[pickRandom(dictFromCSV)]+=1
    generatedDict = {k: v/100. for k,v in newDict.items()}
    print("generated dictionary from my weighted avg code: ", generatedDict)
    bool = True
    for occupations in generatedDict:
        if (dictFromCSV[occupations] - generatedDict[occupations])/dictFromCSV[occupations] >= .2:
            bool = False
    print("meets 20% margin for error" if bool else "does not meet 20% margin for error")

#main()