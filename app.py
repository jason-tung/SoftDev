# azrael - Jason Tung and Hasif Ahmed
# SoftDev1 pd8
# K14 -- Do I Know You?
# 2018-10-02
import string, random, os

from flask import Flask, url_for, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = os.urandom(32) #using os.urandom(32) to generate random number for secret_key

acc = {'Ahmed': 'Tung'} #dictionary to hold user and pass 

@app.route('/')
def hello_world():
    if 'Ahmed' in session: #if ahmed is currently saved 
        return render_template('yes.html',usr = 'Ahmed') #welcome file 
    return render_template('login.html') #login file 

@app.route('/auth', methods=['POST'])
def hello_world2():
    
    if request.form['username'] in acc: 
        if request.form['password'] == 'Tung':
            session['Ahmed'] = 'Tung'
            return redirect(url_for('hello_world'))
        else:
            return render_template('no.html', error = 'password') #if its not the correct pass, return password error
    return render_template('no.html', error = 'username') #if its not the correct user, return username error

@app.route('/logout')
def out():
    session.pop('Ahmed',None) #need none in case theres no 'Ahmed' to pop out 
    return redirect(url_for('hello_world'))

if __name__ == "__main__":
    app.debug = True
    app.run()
