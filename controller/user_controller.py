import flask
from flask import request
from app import app
from model.user_model import user_model
obj = user_model()


@app.route('/user')  
def user_controll():
    return obj.user_model()

@app.route('/user/signup',methods=["POST"])  
def user_add_controll():
    # print(request.form)
    return obj.user_singup_model(request.form)


@app.route('/user/update',methods=["PUT"])   
def user_update_controll():
    # print(request.form)
    return obj.user_update_model(request.form)

