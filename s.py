from re import T
from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def well():
    return "well come"
@app.route('/csss')
def csss():
    return render_template("s.html")
@app.route('/page')
def page():
    return "this is open due to i am add a link in s.html page"
app.run(debug=True)