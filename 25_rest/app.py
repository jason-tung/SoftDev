# azrael - Jason Tung
# SoftDev1 pd8
# K#25 -- Getting More REST
# 2018-11-15

import json
import random

import urllib.request

from flask import Flask, render_template

app = Flask(__name__)

def load(thing):
    return json.loads(urllib.request.urlopen(thing).read())
@app.route('/')
def hello_world():
    cat_fact = load("https://catfact.ninja/fact")
    breed_ll_stub = "https://catfact.ninja/breeds?limit=1&page="
    listy = []
    for x in range(10):
        breed_ll=load(breed_ll_stub + str(random.randint(1,99)))
        listy = listy + breed_ll["data"]
    print(listy)
    return render_template("template.html",your_fact=cat_fact["fact"], data_list=listy)


if __name__ == "__main__":
    app.debug = True
    app.run()
