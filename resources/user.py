from multiprocessing import connection
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username can't be blankk")
    parser.add_argument('password', type=str, required=True, help="password can't be blank")
    
    def post(self):
        data = UserRegister.parser.parse_args()
        res= UserModel.find_by_username(data["username"])
        if res:
            return {"msg": f"user {data['username']} already exist"}, 400
        u = UserModel(**data)
        UserModel.save_to_db(u)
        return {"msg":"user created successfully!!"}, 201

