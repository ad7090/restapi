import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
          self.conn = mysql.connector.connect(host="localhost",password="mysql",user="root",database="flask_test")
          self.conn.autocommit=True
          self.cur = self.conn.cursor(dictionary=True)
          print("db connected") 
        except:
          print("db something worng") 

    def user_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        return json.dumps(result)
    
    def user_singup_model(self,data):
        print(data)
        print(data['name'])
        self.cur.execute(f"INSERT INTO users(name,lastname) VALUES('{data['name']}','{data['lastname']}')")
        result = self.cur.fetchall()
        print(result)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    def user_update_model(self,data):
        print(data)
        print(data['name'])
        print(data['id'])

        self.cur.execute(f"UPDATE users SET name='{data['name']}' , lastname='{data['lastname']}' WHERE id='{data['id']}'")
        # result = self.cur.fetchall()
        # print(self.cur)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201) 