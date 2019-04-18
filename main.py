from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def check_input(login,pw1,pw2):

    name = login
    pass1 = pw1
    pass2 = pw2

    noname = ""
    nopw1 = ""
    nopw2 = ""

    if name == "" or pass1 == "" or pass2 == "":

        if name == "":
            noname = "You didn't enter a Username!  "

        if pass1 == "":
            nopw1 = "You didn't enter a password!  "

        if pass2 == "":
            nopw2 = "You didn't re-enter a password!  "


        return ("Please enter a value in each field. "+ "  " + noname + "  " + nopw1 +"   "+ nopw2+"  ")






@app.route("/register", methods=['POST'])
def user_name():
    username = request.form['user']
    password1 = request.form['password1']
    password2 = request.form['password2']

    username_error = check_input(username, password1, password2)

    if username_error != "":
        return render_template('edit.html', error = username_error)

    match_error = ""

    if password1 != password2:
        match_error = "passwords do not match"
        return render_template('edit.html', error = match_error)
        

    return render_template("confirmation.html",user = username, pw1 = password1, pw2 = password2, error = match_error )


@app.route("/")
def index():
    
    
    return render_template('edit.html')






    
app.run()
