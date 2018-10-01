# azrael - Jason Tung and Hasif Ahmed
# SoftDev1 pd8
# K14 -- Do I Know You?
# 2018-10-02
import string, random, os

from flask import Flask, url_for, render_template, request

app = Flask(__name__)

def ran(n):
    str = ""
    chars = list("1234567890qwertyuiopasdfhgjklzxcvbnm")
    for x in range(n):
        str+=random.choice(chars)
    return str

randUser = ran(5)
randPass = ran(5)


@app.route('/')
def hello_world():
    print(randUser)
    print(randPass)
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def hello_world2():
    if request.form['username'] == randUser and request.form['password'] == randPass:
        return render_template('yes.html', usr=randUser)
    return render_template('no.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
