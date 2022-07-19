from flask import Flask, request
app=Flask(__name__)
@app.route('/forming',method=['POST'])
def login():
    uname=request.form('e')
    password=request.form('p')
    if uname=="arslanansari786.iu@gmail.com" and password=="12345":
     return "welcome"+uname
    else:
        return "try again"
app.run(debug=True)