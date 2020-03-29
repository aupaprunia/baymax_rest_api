from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request
from models.patient_model import ItemModel

class Patient(Resource):

    @jwt_required()
    def get(self,name):
        patient=ItemModel.find_by_name(name)
        if patient:
            return patient.json()
        return {'message':'Patient does not exist'}

    def post(self,name):
        data=request.get_json()
        patient=ItemModel.find_by_name(name)
        if patient:
            return {"message":"Patiet name already exists"}
        
        patient=ItemModel(name, data['hospital_id'])
        patient.save_to_db()
        return {"patient":patient.json()}

    def put(self,name):

        updated_name=request.get_json()
        patient=ItemModel.find_by_name(name)

        if patient:
            patient.name=updated_name['name']
            patient.save_to_db()
            return{"message":"Patient details updated"}
        else:
            if ItemModel.find_by_name(updated_name['name']):
                patient.save_to_db()
                return {"message":"Patient already exists"}
            patient=ItemModel(name,updated_name['hospital_id'])
            patient.save_to_db()
            return{"message":"Patient inserted"}

    def delete(self,name):

        patient=ItemModel.find_by_name(name)
        if patient is None:
            return{"message":"No such patient exists"}

        patient.delete_from_db()
        return{"message":"Patient deleted"}

class all_Patients(Resource):
    def get(self):
        return {'patients':[patient.json() for patient in ItemModel.query.all()]}