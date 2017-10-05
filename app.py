from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(32) #32 bits of random data as a string

username = 'kelly'
password = 'wang'

@app.route("/")
def hello_world():
    
    print session;
    print '_______________________________________________COOKIES GET USERNAME'
    print request.cookies.get('username')
    print "-----------------------ARGS "
    print request.args
    print "-----------------------FORM "
    print request.form

    if request.args["username"] == "kelly":
        if request.args['password'] == 'wang':
            return render_template("form.html")
        else:
            return render_template("form.html", error = 'Wrong Password' )
    else:
        return render_template("form.html", error = "Wrong Username")
    
    session['username']=request.args['username']
    session['password']='wang'
    
    return render_template('form.html')

@app.route("/hello")
def hello():
    return 'hi'

if __name__ == "__main__":
    app.debug = True
    app.run()
