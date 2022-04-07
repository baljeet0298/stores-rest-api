from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

from resources.user import UserRegister
from resources.item import ItemList, Item
from resources.store import StoreList, Store

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
#turn off flask modification tracking 
app.config['SQLALCHEMy_TRACK_MODIFICATIONS']=False
#to encrypt and decrypt tokens
app.secret_key = "jose"
api=Api(app)

#before the first request run it is gonna create data.db and create all tables unless it exist there
@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port = 4998, debug=True)