from flask import Flask, request, render_template, redirect
import os
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def signup_form():
    return render_template('main.html')

@app.route("/signup", methods=['POST'])
def user_signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) == 0 or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "Not a valid username"
    
    if len(password) == 0 or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "Not a valid password"
    
    if verify != password:
        verify_error = "Passwords don't match"

    if len(email) > 0:
        if len(email) < 3 or len(email) > 20 or ' ' in email:
            email_error = "Not valid, must be between 3-20 characters"
        elif email.count('@') != 1 or email.count('.') != 1:
            email_error = "Must contain '@' and '.'"

    if username_error == "" and password_error == "" and verify_error == "" and email_error == "":
        return redirect('/welcome?username='+username)
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, verify_error=verify_error, email_error=email_error, email=email)

@app.route("/welcome")
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()