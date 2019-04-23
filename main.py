from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


# checks email input for all validation requirements
def check_email(login_name):

    name = login_name

    user_error = ""
   
    if len(name) < 3:
        user_error = "Input is too short. Must be more than 3 characters"
    elif len(name) > 20:
        user_error = "Input is too long. Must be less than 20 characters"
    elif " " in name:
        user_error = "Input can't contain a space!!"
    elif name.count("@") == 0:
        user_error = "Email must include an '@' symbol"
    elif name.count("@") > 1:
        user_error = "Email can only include one '@' symbol"
    elif name.count(".") == 0:
        user_error = "Email must include an '.' symbol"
    elif name.count(".") > 1:
        user_error = "Email can only include one '.' symbol"
    
    



    return (user_error)




# checks user input for character length requirements and bad tokens
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

    # catches all inputs from forms
    username = request.form['user']
    password1 = request.form['password1']
    password2 = request.form['password2']
    email_address = request.form['email']
    
    #validates all input
    user_errors = check_input(username)
    password1_error = check_input(password1)
    password2_error = check_input(password2)

    # creates empy strings for email and password match error. If no errors 
    # caught this will prevent these errors rom rendering on the final html page
    email_errors = ""
    match_error =""


    # checks for any input in email form. If input present the data is validated
    if email_address != "":

        email_errors = check_email(email_address)

    
    #checks to see if passwords entered in password and re-enter password field match
    if password1 != password2:

        match_error = "passwords do not match"


    # clears username input if there is a user name validation error
    if user_errors != "":
        username = ""

    # clears email input if there is a email name validation error
    if email_errors != "":
        email_address = ""



    # renders template if any errors are caought during input validation
    if email_errors != "" or user_errors != "" or password1_error != "" or password2_error != "" or match_error != "":
        return render_template('edit.html', pass1_error = password1_error, pass2_error = password2_error, matching_error = match_error,
         username_error = user_errors, email_error = email_errors, username = username, email = email_address)

    
    # if no errors are caught the confirmation page will display
    return render_template("confirmation.html",user = username )


@app.route("/")
def index():
    
    
    return render_template('edit.html')






    
app.run()
