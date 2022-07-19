from email import message
from flask import Flask, render_template, request, session
app=Flask(__name__)
app.secret_key="abc"
@app.route('/')
def home():
    return "wellcome to my site"
@app.route('/log')
def log():
    return render_template('loginout.html')
@app.route('/logout')
def logout():
    session.pop('EMAIL',None)
    return render_template('loginout.html')
@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        userE=request.form['E']
        userP=request.form['p']
        if userE=="arslan@gmail.com" and userP=="1234":
            session['EMAIL']=userE
            return render_template('success.html',EMAIL=userE)
        else:
            msg="ERROR:invalid Email and password please try again"
            return render_template('loginout.html',message=msg)
app.run(debug=True)