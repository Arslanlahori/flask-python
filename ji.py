from dis import disco
from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return "wellcome"
@app.route('/<int:score>')
def scoree(score):
    return render_template('score.html',myscore=score)
@app.route('/result')
def result():
    dict={"english":87,"physices":80,"math":89,"urdu":85,"chemistry":83,"pakstudy":48}
    return render_template("score.html",fresult=dict)
app.run(debug=True)