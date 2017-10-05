#Kelly Wang and Jawadul Kadir
#SoftDev1 pd7
#HW7 -- Do I Know You?
#2017-10-04

from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(32) #32 bits of random data as a string

#hardcoded login credentials
username = 'kelly'
password = 'wang'

#root route leads to form if not logged in,
#or to welcome page if logged in.
@app.route("/")
def hello_world():
	if 'username' in session:
		return render_template("hello.html", username = 'kelly')
	return render_template('form.html')

#welcome page
@app.route("/hello", methods=["POST"])
def hello():
	print session;
	print '_______________________________________________COOKIES GET USERNAME'
	print request.cookies.get('username')
	print "-----------------------ARGS "
	print request.args
	print "-----------------------FORM "
	print request.form

	#checks if login credentials are correct
	if request.form["username"] == "kelly":
		if request.form['password'] == 'wang':
		    session['username'] = request.form['username']
		    session['password'] = request.form['password']
		    print session
		    return render_template("hello.html", username = request.form['username'])
		else:
		    return render_template("form.html", error = 'Wrong Password' )
	else:
	    return render_template("form.html", error = "Wrong Username")

	#session['username']=request.form['username']
	#session['password']='wang'
	return render_template('hello.html')

#exit page
@app.route("/goodbye", methods=["POST"])
def goodbye():
	#logs out user
	session.pop('username')
	session.pop('password')
	return render_template("form.html", error = 'bye')

if __name__ == "__main__":
	app.debug = True
	app.run()
