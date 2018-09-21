from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return (" I DO NOT LIKE WAA")

@app.route('/my_foist_template')
def e():
    return render_template("template0.html", my_title="boo!", collection=[0,1,1,2,3,5,8])

app.debug = True
app.run()
