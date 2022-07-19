from flask import Flask, redirect, render_template, request, url_for
app=Flask(__name__)
@app.route('/')
def home():
    return "this is show flash msg and redirect the function"
@app.route('/form')
def show():
    return render_template('forming.html')
@app.route('/login' ,methods=['POST'])
def enter():
    if request.method=='POST':
     email=request.form['e']
     password=request.form['p']
     if email=="arslanansari786.iu@gmail.com" and password=="123456":
        return "you login"
     else:
        return redirect (url_for('show'))
        
app.run(debug=True)