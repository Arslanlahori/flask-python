from app import app
from classes.main import crud
from flask import request
obj=crud()

print("ab compiler function.py me agya hy\n")


#this function is used to create table in database
@app.route('/create')
def create_table():
    print("compiler create_table  function me agya hy ")
    return obj.createtable()



#this is used to insert data in database
@app.route('/insert',methods=['POST'])
def insert():
    print("compiler insert function me agya hy")
    data=request.form
    print(data)
    print(data.__dict__)
    return obj.insertdata(data)



#this is used to update data    
@app.route('/update',methods=['PUT'])
def update():
    print("compiler update function me agya hy")
    data=request.form
    print(data)
    return obj.updatedata(data)


#this is read data from database or Get data from database
@app.route('/fetch')
def fetch():
    print("ab compiler fetch me hy\n")
    return obj.fetchdata()

#this function is used for fetch data by putting id in body of postman
@app.route('/fetchp')
def fetchp():
    print("ab compiler fetchp me hy\n")
    data=request.form
    print(data)
    return obj.fetchpdata(data)




@app.route('/fetchid/<id>')
def fetchid(id):
    print("ab compiler fetchid function  me hy\n")
    return obj.fetchdataid(id)


#this function is used for delete row by id putting id in url
@app.route('/delete/<id>',methods=['DELETE'])
def delete(id):
    print("compiler delete function me agya hy")
    print(id)
    return obj.deletedata(id)


#this function is used for delete row by id putting id in body of postman
@app.route('/deletep',methods=['DELETE'])
def deletep():
    print("compiler deletep function me agya hy")
    data=request.form
    print(data)
    return obj.deletepdata(data)



#this is used to drop table
@app.route('/Droptable',methods=['DELETE'])
def Drop():
    print("compiler drop function me agya hy")
    return obj.droptable()
