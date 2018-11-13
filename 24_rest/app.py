# azrael - Jason Tung
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-14
import json
import urllib

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
    print(url)
    data = json.loads(url.read().decode())
    print(data)


if __name__ == "__main__":
    app.debug = True
    app.run()
