# azrael - Jason Tung and YinOn Chan
# SoftDev1 pd8
# K10 -- <<<FILL THIS OUT>>>
# 2018-09-21

import occupy
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    f = occupy.convert("data/occupations.csv")
    return (render_template("occupyTemplate.html",random_occupation=occupy.pickRandom(f),dict=f.items()))

app.debug = True
app.run()