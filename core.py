from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import dotenv
import os
from subscribe import subscriber

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_KEY')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/add_subscriber", methods=['POST'])
def add_subscriber():
    email = request.form['email']
    payload = {
        'API_KEY':os.getenv('MAIL_CHIMP_KEY'),
        'LIST_ID':os.getenv('LIST_ID'),
        'SERVER_PREFIX':os.getenv('SERVER_PREFIX'),
        'SUB_EMAIL':email
    }
    subscriber(payload)
    flash("Subscribed successfully!")
    return redirect(url_for('index'))

@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == "__main__":
    app.run(debug=True)