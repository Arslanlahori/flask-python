from flask import Flask
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']='3306'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='alpha'
mysql=MySQL(app)
# @app.route('/')
# def home():
#     return "this show how we insert data into table in database using flask"
@app.route('/create')
def create():
    query="CREATE TABLE crops(cropid int primary key,cropname varchar(20),cropcolor varchar(10))"
    cur=mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return "done"
    


# i created table name users in database login
# @app.route('/insert')
# def index():
#     firstname="arslan" 
#     lastname="arshad"
#     cur=mysql.connection.cursor()
#     cur.execute("INSERT INTO users(fname,lname) VALUES(%s,%s)",(firstname,lastname))
#     mysql.connection.commit()
#     cur.close()
#     return "inserted"
# @app.route('/fetch')
# def fetch_data():
#     query="select * from book"
#     cur=mysql.connection.cursor()
#     cur.execute(query)
#     mysql.connection.commit()
#     result=cur
#     for x in result:
#             print(x)

app.run(debug=True)