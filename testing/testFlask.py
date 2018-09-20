from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("about to print __name...")
    print(__name__)
    return "No hablo questo!"



if __name__ == "main":
    app.debug = True
    app.run()