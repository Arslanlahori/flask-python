from flask import Flask, make_response, request
app=Flask(__name__)
@app.route('/')
def home():
    return "this is used to set cookies get cookies "
@app.route('/set')
def setcoki():
    set=make_response("cookies is set")
    set.set_cookie('name=frame','value=falsk')
    return set
@app.route('/gett')
def getcooki():
    gett=request.cookies.get('name=frame')
    #return gett
app.run(debug=True)