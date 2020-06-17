from flask import Flask,render_template,request,url_for
from flask_cors import CORS
from pymongodb import DB_data

app = Flask(__name__)

CORS(app)

@app.route('/', methods = ["GET","POST"])

def index():

    if request.method == "GET":
        pass
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("pwd")
        DB_data(name,email,password)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
