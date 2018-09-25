# azrael - Jason Tung and YinOn Chan
# SoftDev1 pd8
# K10 -- Jinja Tuning
# 2018-09-21

import occupy
from flask import Flask, render_template
app = Flask(__name__)

#homepage instantly redirects to occupation
@app.route("/")
def dog():
    return ('''<html><head><meta http-equiv="refresh" content="0; URL='/occupations'" /></headZ></html>''')

#take my occupy tmeplate in my templates folder and pass in a random occupation as well as the dictionary for the values (link + percentage)
@app.route("/occupations")
def main():
    f = occupy.convert("data/occupations.csv")
    return (render_template("occupyTemplate.html",random_occupation=occupy.pickRandom(f),dict=f))

#RUN IT!!!
app.debug = True
app.run()