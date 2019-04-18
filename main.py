from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def check_username(login_name):

    name = login_name

    user_error = ""
   
    if name == "":
        user_error = "Please enter a username"
    elif len(name) < 3:
        user_error = "Username is too short. Must be more than 3 characters"
    elif len(name) > 20:
        user_error = "Username is too long. Must be less than 20 characters"
    



    return (user_error)






@app.route("/register", methods=['POST'])
def user_name():
    username = request.form['user']
    password1 = request.form['password1']
    password2 = request.form['password2']

    user_errors = check_username(username)



    if user_errors != "":
        return render_template('edit.html', error = user_errors, username_error = user_errors)

    

    return render_template("confirmation.html",user = username, pw1 = password1, pw2 = password2 )


@app.route("/")
def index():
    
    
    return render_template('edit.html')






    
app.run()
