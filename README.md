# flask-python
flask python paractice

confuse add or not

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'alpha'
mysql = MySQL(app)


@app.route('/')
def method_name():
    return "this program is used to fetch data fron database and show on browser"

#CREATE TABLE 
@app.route('/create')
def create_table():
    query = "CREATE TABLE if not exist onecrop(id int primary key , name varchar(20), color varchar(20), area int)"
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return "Created Successfully"

#INSERT FUNCTION
@app.route('/insert')
def insert():
    query = "INSERT INTO onecrop(id,name,color,area) VALUES(%s,%s,%s,%s)"
    cr = [(1, "wheat", "yellow", 3000), (3, "okra", "Green", 4000)]
    cur = mysql.connection.cursor()
    cur.executemany(query, cr)
    mysql.connection.commit()
    cur.close()
    return "Inserted Successfully"
    
#update function   
@app.route('/update/<upn>/<cn>')
def update(upn, cn):
    query = ("UPDATE onecrop SET name='{}' WHERE name='{}'".format(upn, cn))
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return "Update Data Successfully "
#CROP OF LIST
@app.route('/fetch/list')
def fetchlist():
    query = "SELECT * FROM onecrop "
    cur = mysql.connection.cursor()
    cur.execute(query)
    show = cur.fetchall()
    return render_template("onecroptable.html", show=show)

#FETCH FUNCTION BY ID
@app.route('/fetch/<a>')
def fetch(a):
    query = ("SELECT * FROM onecrop WHERE id={}".format(a))
    cur = mysql.connection.cursor()
    cur.execute(query)
    show = cur.fetchall()
    return render_template("onecroptable.html", show=show)
    
#FETCH FUNCTION BY NAME
@app.route('/fetch/<n>')
def fetch(n):
    query = ("SELECT * FROM onecrop WHERE name='{}'".format())
    cur = mysql.connection.cursor()
    cur.execute(query)
    show = cur.fetchall()
    return render_template("onecroptable.html", show=show)
   
#DELETE FUNCTION BY NAME
@app.route('/delete/<nd>')
def delete(nd):
    query = ("DELETE FROM onecrop WHERE  name='{}'".format(nd))
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    return "Deleted Successfully"    
    
#DELETE FUNCTION BY ID
@app.route('/delete/<b>')
def delete(b):
    query = ("DELETE FROM onecrop WHERE  id={}".format(b))
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    return "Deleted Successfully"


app.run(debug=True)
