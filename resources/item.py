from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="price field should have data")
    parser.add_argument('name', type=str, required=True, help="name field should have data")
    parser.add_argument('store_id', type=int, required=True, help="store id field should have data")
        
    @jwt_required()
    def get(self, name):
        row = ItemModel.find_by_name(name)
        if row:  
            return row.json(), 200
        return {"msg": "item not found"}, 404

    @jwt_required()
    def post(self, name):
        res = ItemModel.find_by_name(name)
        if res:
            return {"msg": f"An item with name {name} already exist"}, 400
        req_data = Item.parser.parse_args()
        i = ItemModel(**req_data)
        i.save_to_db()
        return {"msg":"item created successfully!!"}, 201


    @jwt_required()
    def put(self, name):
        req_data = Item.parser.parse_args()
        _, res = self.get(name)
        i=ItemModel(**req_data)
        if res==200:
            i.save_to_db()
            return {"msg": "item updated"}, 200
        else:
            i.save_to_db()
            return {"msg": "item created"}, 201
        
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
            return {"msg": "item deleted"}, 200
        return {"msg": "item not found"} , 404    

class ItemList(Resource):
    @jwt_required()
    def get(self):
        res = ItemModel.find_all()
        return {"items" : [i.json() for i in res]}, 200
        # return {"items": list(map(lambda x: x.json(), res))}