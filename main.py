from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too








@app.route("/register", methods=['POST'])
def user_name():
    username = request.form['user']
    password1 = request.form['password1']
    password2 = request.form['password2']

    if password1 != password2:
        error = "passwords do not match"
        return redirect("/?error"+error)

    return render_template("confirmation.html",user = username, pw1 = password1, pw2 = password2 )


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    
    return render_template('edit.html',error = encoded_error and cgi.escape(encoded_error, quote=True))




    
app.run()
