# azrael - Jason Tung
# SoftDev1 pd8
# K13 -- Echo Echo Echo
# 2018-09-28

# username entered
# request method used
# your greeting to this person

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(app)
    return (render_template("doggy.html"))

@app.route('/auth')
def hello_world1():
    print("app: ", app)
    print("request: ", request)
    print("args: " ,request.args)
    print("req.args indexed", request.args['usrname'])
    print("req.form indexed", request.form['usrname'])
    print("FFFDSFDSKFJKDSNFJKDSNFJKDNSKJF")
    return (render_template("kitt.hyml", username=request.args['usrname'], method=request.method))

if __name__ == "__main__":
    app.debug = True
    app.run()
