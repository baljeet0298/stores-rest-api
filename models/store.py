from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')
    
    def __init__(self, name) -> None:
        self.name=name
    
    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}

    def save_to_db(self):
        #session is collection of object that are going to write to database, we add obj to session it write to db 
        db.session.add(self)
        db.session.commit()
        return {"msg": "save to db"}, 201
        #this code can update and insert both
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()