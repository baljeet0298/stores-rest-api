from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"msg": "store is already there with name {}".format(name)}, 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201
        
    def get(self, name):
        store =StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404
        

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete()
            return {"msg": "store deleted"}
        return {"msg": "store is not there in db"}

class StoreList(Resource):
    def get(self):
        return {"store": [x.json() for x in StoreModel.query.all()]}
        