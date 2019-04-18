from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def check_input(login_name):

    name = login_name

    user_error = ""
   
    if name == "":
        user_error = "Please enter a value"
    elif len(name) < 3:
        user_error = "Input is too short. Must be more than 3 characters"
    elif len(name) > 20:
        user_error = "Input is too long. Must be less than 20 characters"
    elif " " in name:
        user_error = "Input can't contain a space!!"
    



    return (user_error)






@app.route("/register", methods=['POST'])
def user_name():
    username = request.form['user']
    password1 = request.form['password1']
    password2 = request.form['password2']

    user_errors = check_input(username)
    password1_error = check_input(password1)
    password2_error = check_input(password2)

    match_error =""

    if password1 != password2:

        match_error = "passwords do not match"



    if user_errors != "" or password1_error != "" or password2_error != "" or match_error != "":
        return render_template('edit.html', pass1_error = password1_error, pass2_error = password2_error, matching_error = match_error,
         username_error = user_errors, username = username)

    

    return render_template("confirmation.html",user = username )


@app.route("/")
def index():
    
    
    return render_template('edit.html')






    
app.run()
