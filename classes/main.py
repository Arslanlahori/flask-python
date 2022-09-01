import mysql.connector
from flask import jsonify



class crud():
    print("ab compiler class me hy \n")
    
    def __init__(self):
       try:
        #connection esteblish code
            
            self.con=mysql.connector.connect(host="localhost",
                                        port=3306,
                                        user="root",
                                        password="",
                                        database="crud_operation"
                                        )
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            
            print("successfully python connected  with mysql ")
       except:
           
               print("some error")
           
           
    
    def createtable(self):
        print("compiler class the method createtable me agya hy")
        query = "CREATE TABLE IF NOT EXISTS operation(id int , name varchar(20), color varchar(20), area int)"
        self.cur.execute(query)
        
        return "Table Created Successfully"
    
    
    def insertdata(self,data):
        print("compiler class ke method insertdata me agya hy")
        print(data)
        print("to print specific value")
        print(data['name'])
        query = (f"INSERT INTO operation(id,name,color,area) VALUES({data['id']},'{data['name']}','{data['color']}',{data['area']})")
        self.cur.execute(query)
        return "Inserted Successfully"
    
    
    
    def updatedata(self,data):
        print("compiler class ke method updatedata me agya hy")
        print(data)
        query = (f"UPDATE operation SET id={data['id']},name='{data['name']}',color='{data['color']}',area={data['area']} Where id={data['id']}")
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return "Data is updated"
        else:
             return "Data is not update because this id is not present"
         
         
    
    def fetchdata(self):
        print("compiler class ke method fetchdata me agya hy")
        query = "SELECT * FROM operation "
        self.cur.execute(query)
        result=self.cur.fetchall()
        print(result)
    
        if len(result)>0:
            return jsonify(result)
        else:
             return "No data is found"  
     
     
    def fetchpdata(self,data):
        print("compiler class ke method fetchpdata me agya hy")
        query = (f"SELECT * FROM operation WHERE  id={data['id']}")
        self.cur.execute(query)
        result=self.cur.fetchall()
        print(result)
    
        if len(result)>0:
            return jsonify(result)
        else:
             return "No data is found"     
         
    def fetchdataid(self,data):
        print("compiler class ke method fetchdataid me agya hy")
        query = (f"SELECT * FROM operation WHERE id={data}")
        self.cur.execute(query)
        result=self.cur.fetchall()
        print(result)
    
        if len(result)>0:
            return jsonify(result)
        else:
             return "No data is found"  
         
         
         
         
    def deletedata(self,id):   
        print("compiler class ke method deletedata me agya hy") 
        print(id)
        query = (f"DELETE FROM operation WHERE id={id}")
        self.cur.execute(query)
    
        if self.cur.rowcount>0:
            return "Data is Deleted"
        else:
             return "Data is not Deleted because this id is not present"
         
         
    def deletepdata(self,data):   
        print("compiler class ke method deletepdata me agya hy") 
        print(data)
        query = (f"DELETE FROM operation WHERE id={data['id']}")
        print(query)
        self.cur.execute(query)
    
        if self.cur.rowcount>0:
            return "Data is Deleted"
        else:
             return "Data is not Deleted"
             
  
    
    
    def droptable(self):
        print("compiler class ke method droptable me hy")
        query = "DROP TABLE IF EXISTS operation "
        self.cur.execute(query)
        
        return "Table Droped Successfully"
    