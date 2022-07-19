from pickle import TRUE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/alpha'
app.config['SQLALCHEMY_MODIFICATIONS']=True
db = SQLAlchemy(app)
class crop(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    color = db.Column(db.String(120))
    disease = db.Column(db.String(30))
@app.route('/')
def index():
    fname="wheet"
    rang="yellow"
    bimari="canker"
    query=crop(name=fname,color=rang,disease=bimari)
    db.session.add(query)
    db.session.commit()
    return "sucess"
# @app.route('/fetch')
# def fetch():
#     cur=db.cursor()
#     query="SELECT * FROM user"
#     cur.execute(query)
#     result=cur.fetchall()
#     return "fetch"
#     # for x in result:
#     #     print(x)
app.run(debug=True)