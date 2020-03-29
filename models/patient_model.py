from db import db

class ItemModel(db.Model):

    __tablename__='patients'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))

    hospital_id=db.Column(db.Integer, db.ForeignKey('hospitals.id'))
    hospital=db.relationship('HospitalModel')

    def __init__(self, name, hospital_id):
        self.name=name
        self.hospital_id=hospital_id

    def json(self):
        return{"Name":self.name}

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