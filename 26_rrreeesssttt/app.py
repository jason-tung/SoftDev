# azrael - Jason Tung
# SoftDev1 pd8
# K#26 -- Getting More REST
# 2018-11-16

import json
import random

import urllib.request

from flask import Flask, render_template

app = Flask(__name__)

def load(thing):
    return json.loads(urllib.request.urlopen(thing).read())

def get_breed(links):
    my_dict = {}
    for link in links:
        small_ary = link.split("/")
        #print(small_ary)
        breed_index = small_ary.index("breeds")
        my_dict[small_ary[breed_index+1]] = link
    #print(my_dict)
    return my_dict

@app.route('/')
def hello_world():
    rand_dog = load("https://random.dog/woof.json")
    bored_api = load("https://www.boredapi.com/api/activity")
    poodle_pics = load("https://dog.ceo/api/breed/poodle/images/random/2")
    dog_pics=load("https://dog.ceo/api/breeds/image/random/2")
    big_ary = []
    for x in poodle_pics["message"]:
        big_ary.append(x)
    for x in dog_pics["message"]:
        big_ary.append(x)
    print(poodle_pics)
    print("----------")
    print(dog_pics)
    print("----------")
    print(big_ary)
    dogs = get_breed(big_ary)

    return render_template("template.html",dog = rand_dog["url"], bored_dict = bored_api, dogs = dogs)


if __name__ == "__main__":
    app.debug = True
    app.run()
