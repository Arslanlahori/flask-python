from flask import Flask, redirect, render_template, request,url_for
app=Flask(__name__)
app.secret_key = "login"
@app.route('/')
def home():
    return "this flask site is used to upload a video or file"
@app.route('/upload',methods=['GET'])
def upload():
    if request.method=='GET':
     fl=request.args.get('file')
     fl.save('static/',fl.fiename)
     return redirect(url_for('home'))
app.run(debug=True)