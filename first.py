from flask import Flask, redirect, render_template, url_for
app=Flask(__name__)
@app.route('/')
def wellcome():
    return "this is wellcome pages"
@app.route('/arslan')
def auther():
    return "Arslan is the owner of the application"
@app.route('/<nam>')
def users(nam):
    return "i am the user " + nam
@app.route('/student')
def student():
    return "<html><body><h1>this is student here</h1></body></html>"
@app.route('/faculty')
def faculty():
    return "this is faculity here"
@app.route('/user/<name>')
def user(name):
    if name=="student":
        return redirect(url_for("student"))
    if name=="faculty":
        return redirect(url_for("faculty")) 
@app.route('/page')
def pages():
    return render_template("index.html")  

app.run(debug=True)