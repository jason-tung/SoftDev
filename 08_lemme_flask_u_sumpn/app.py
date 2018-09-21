# Jason Tung 
# SoftDev1 pd8
# K8 -- Fill Yer Flask 
# 2018-09-19


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("about to print __name...")
    print(__name__)
    return "here is... <a href = 'wee''> DA NEXT PAGE </a><br>No hablo questo!<br><img src = 'https://www.shitpostbot.com/img/sourceimages/buff-cat-589a092def00a.jpeg'>"

@app.route("/wee")
def oops():
    print("console.log('hi console!') : - )")
    return ("""<a href = "owo"> hey buddie :- ) </a>""")

@app.route("/owo")
def weeeee():
    return('<a href = https://www.youtube.com/watch?v=5IsSpAOD6K8> this is the end of the road, cowboy </a>')

@app.route("/yinange")
def poeioe():
    with open("static/hey.html", 'r') as fin:
        return fin.read()




if __name__ == "__main__":
    app.debug = True
    app.run()
