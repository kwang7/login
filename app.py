from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    if session['username'] == 'kelly':
        if session['password'] == 'wang':
            return render_template("hello.html")
        else:
            return render_template("goodbye.html")
    else:
        return render_template("goodbye.html")

    app.secret_key = os.urandom(32) #32 bits of random data as a string
    #print session
    session['username']=request.args['username']
    session['password']='wang'
    print '_______________________________________________COOKIES GET USERNAME'
    print request.cookies.get('username')

    return render_template('form.html')

#@app.route("/hello")
#def hello():


if __name__ == "__main__":
    app.debug = True
    app.run()
