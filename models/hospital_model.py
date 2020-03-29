from db import db

class HospitalModel(db.Model):

    __tablename__='hospitals'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))

    patients=db.relationship('ItemModel', lazy='dynamic')

    def __init__(self,name):
        self.name=name

    def json(self):
        return{"Name":self.name,"patients":[patient.json() for patient in self.patients.all()]}

    @classmethod
    def find_by_name(cls, name):
        patient=cls.query.filter_by(name=name).first()
        return patient
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()