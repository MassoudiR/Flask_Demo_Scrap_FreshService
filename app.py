from flask import Flask,render_template,request
import data1

app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def home():
    if request.method=="POST":
        email = request.form.get('Email')
        passowed = request.form.get('Password')
        Ticket_ID = request.form.get('Ticket_ID')
        remember_me = request.form.get('remember_me')
        print(email)
        print(passowed)
        print(Ticket_ID)
        print(remember_me)
        return('OK ! ....')
        
        ##data1.freshservice()
        
    return render_template('index.html')
