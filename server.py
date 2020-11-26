from flask import Flask, render_template, request,url_for, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/work')
def work():
    return render_template("work.html")

@app.route('/works')
def works():
    return render_template("works.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

def write_file(data):
    with open("database.txt",mode="a") as file:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        x = file.write(f"\n{email},{subject},{message}")

def write_csv(data):
    with open("database.csv",mode="a",newline='') as file2:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        x = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        x.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        #write_file(data)
        write_csv(data)
        #print(data)
        return render_template("thankyou.html")
    else:
        return "Something is went wrong"
