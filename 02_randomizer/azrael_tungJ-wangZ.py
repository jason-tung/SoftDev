# azrael - Zane Wang and Jason Tung
# SoftDev1 pd8
# K02 -- NO-body expects the Spanish Inquisition!
# 2018-09-11

import random

KREWES = {

        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia',
              'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang',
              'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent',
              'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ',
              'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin',
              'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal',
              'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo',
              'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed',
              'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin',
              'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex',
              'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas',
              'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ',
              'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry',
              'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']

}

def randomizer(team):
    ''' returns a random value from a given key of the dictionary KREWES '''
    return random.choice(KREWES[team])

#testing the function
print (randomizer('x'))
list = ['w','m','x']
tester = True
for letter in list:
    bool = (randomizer(letter) in KREWES[letter])
    tester &= bool
    print(bool)
print("all cases passed" if tester else "one or more cases failed")