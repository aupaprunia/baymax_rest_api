import sqlite3
from flask_restful import Resource
from flask import request
from models.user_model import User

class UserRegister(Resource):
    def post(self):
        data=request.get_json()
        
        if User.find_by_username(data['username']):
            return{"message":"User already exists"}

        user=User(data['username'],data['password'])
        user.save_to_db()
        
        return{"message":"User Created"}