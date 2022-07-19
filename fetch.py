from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def home():
    return " this flask site is used to fetch data"
@app.route('/input')
def form():
    return render_template('formm.html')
@app.route('/output',methods=['POST'])
def print():
    user=request.form
    return render_template('result.html', result=user)
app.run(debug=True)