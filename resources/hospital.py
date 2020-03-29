from flask_restful import Resource
from models.hospital_model import HospitalModel

class Hospital(Resource):
    def get(self, name):
        hospital= HospitalModel.find_by_name(name)
        if hospital:
            return hospital.json()
        return {'message':'Hospital Not Found'}

    def post(self,name):
        hospital= HospitalModel.find_by_name(name)
        if hospital:
            return{'message':'Hospital with this name already exists'}
        hospital=HospitalModel(name)
        hospital.save_to_db()
        return {'message':'Hospital Created'}

    def delete(self, name):
        hospital= HospitalModel.find_by_name(name)
        if hospital:
            hospital.delete_from_db()
            return{'message':'Hospital Deleted'}
        return{'message':'Hospital Does not Exist'}

class all_Hospitals(Resource):
    def get(self):
        return {'hospitals':[hospital.json() for hospital in HospitalModel.query.all()]}