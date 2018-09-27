# azrael - Jason Tung and <<<NAME>>>
# SoftDev1 pd8
# K<<NUMBER>> -- <<<FILL THIS OUT>>>
# <<YEAR-MON-DAY>>

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return (render_template("doggy.html"))

if __name__ == "__main__":
    app.debug = True
    app.run()
