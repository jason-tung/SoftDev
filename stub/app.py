# azrael - Jason Tung and <<<NAME>>>
# SoftDev1 pd8
# K<<NUMBER>> -- <<<FILL THIS OUT>>>
# <<YEAR-MON-DAY>>

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.debug = True
    app.run()
