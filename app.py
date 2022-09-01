# first two line http server banati hyn jo url me 5000 likha hota hy is ko hit karti hyn


from flask import Flask

app = Flask(__name__)


# jo b method '@' is se start ho is ko decorator khty hyn
# in function me se phily decorator call hoga phir us k bad welcome function call hoga


@app.route('/')
def welcome():
    print("now compiler is in welcome function")
    return """Write functions to create,get,update,delete item and one function to get all the items\n.
              Return output in json format.All functions will test using postman."""

from controler import *



if __name__ == '__main__':
    app.run(debug=True)