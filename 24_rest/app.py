# azrael - Jason Tung
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-14

import json

import urllib.request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
    data = json.loads(url.read())
    print(data)
    return render_template("template.html",img=data["url"],planet=data["resource"]["planet"], date = data["date"])


if __name__ == "__main__":
    app.debug = True
    app.run()
