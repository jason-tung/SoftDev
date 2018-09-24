# azrael - Jason Tung and YinOn Chan
# SoftDev1 pd8
# K10 -- Jinja Tuning
# 2018-09-21

import occupy
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    #make the dictionary occupation : [%,link]
    f = occupy.convert("data/occupations.csv")
    #make website pass template vars
    return (render_template("occupyTemplate.html",random_occupation=occupy.pickRandom(f),dict=f))

app.debug = True
app.run()