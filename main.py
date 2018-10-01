from flask import Flask, request,redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('userid.html')

@app.route("/", methods=['POST'])
def validate_inputs():

    user_name = ""
    user_email = ""
    error_name = ""
    error_password = ""
    error_verify_password = ""
    error_email = ""

    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        verify_password = request.form['verify_password']
        user_email = request.form['user_email']

        #test to see if there is a blank form or enough characters in the form
        for char in user_name:
            if char.isspace():
                error_name = "Please re-enter your Username"
                user_name = ''
            else:
                if (len(user_name)<3) or (len(user_name)>20):
                    error_name = "The Username needs to be between 3-20 characters"
                    user_name = ''

        if not user_name:
            error_name = "Please enter a valid Username"
            user_name = ""

        if user_name == '':
            error_name = "Please enter a valid username."
            user_name = ''


        #test to see if there are any spaces and that the passwords match
        for char in user_password:
            if char.isspace():
                error_password = "Password cannot contain spaces"
            elif (len(user_password)<3) or (len(user_password)>20):
                error_password = "Password must be 3 to 20 characters without spaces"
            elif not len(user_password):
                error_password = "Pleae enter a valid password"

        if user_password != verify_password:
            error_verify_password = "The passwords do not match"

        #test for a valid email entered by the user
        
        if user_email == '':
            error_email = ""
        elif "@" not in user_email:
            error_email = "This is not a valid email address"
        elif "." not in user_email:
            error_email = "This is not a valid email address"
        elif " " in user_email:
            error_email = "This is not a valid email address"
        elif len(user_email)<3 or len(user_email)>20:
            error_email = "This email is too long for our form"


        #check each to see if there are errors and render proper form
        if (not error_name) and (not error_password) and (not error_verify_password) and (not error_email):
            return render_template ('finalform.html', user_name = user_name)
        else:
            return render_template('userid.html', user_name = user_name, user_email = user_email, 
                            error_name = error_name, error_password = error_password, 
                            error_verify_password = error_verify_password, error_email = error_email)


app.run()