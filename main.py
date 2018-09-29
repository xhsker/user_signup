from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/", methods=['POST', 'GET'])
def input_info():

    #making sure to get the errors set to an empty string to give the user an error
    #if they don't fill out form completely

    user_name = ""
    user_email = ""
    error_name = ""
    error_password = ""
    error_verify_password = ""
    error_email = ""

    #makes sure to get a "POST" request from the browser

    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        verify_password = request.form['verify_password']
        user_email = request.form['user_email']

        #test to see if there is a blank form or enough characters in the form
        for char in username:
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


        #test to see if there are any spaces and that the passwords match
        for char in user_password:
            if char.isspace():
                error_pass = "Password cannot contain spaces"
            else:
                if (len(user_password)<3) or (len(user_password)>20):
                    error_pass = "Password must be 3 to 20 characters without spaces"

        if not len(user_password):
            error_pass = "Pleae enter a valid password"

        if user_password != verify_password:
            error_verify_password = "The passwords do not match"

        #test for a valid email entered by the user
        if (user_email !="") and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.+$', user_email)):
            error_email = "Please enter a valid email"
            user_email = ""

        #check each to see if there are errors
        if (not error_name) and (not error_pass) and (not error_verify_password) and (not error_email):
            return redirect('/answer?user_name={0}'.format(user_name))

    return render_template('userid.html', user_name = user_name, user_email = user_email, 
                            error_name = error_name, error_pass = error_pass, 
                            error_verify_password = error_verify_password, error_email = error_email)


    @app.route('/answer')
    def answer():

        user_name = request.args.get('user_name')
        return render_template('finalform.html', user_name = user_name)




        run.app()
