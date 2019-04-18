from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too






@app.route("/crossoff", methods=['POST'])
def crossoff_movie():

   
    return redirect("/")

@app.route("/add", methods=['POST'])
def add_movie():
    

    return redirect("/")


@app.route("/")
def index():
    # encoded_error = request.args.get("error")
    return render_template('edit.html')



    
app.run()
