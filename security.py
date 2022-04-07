from models.user import UserModel
from werkzeug.security import safe_str_cmp


# users = [
#     User(1,"bob","sfsa")
# ]

# username_mapping = {i.username:i for i in users}

# userid_mapping = {i.id:i for i in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password,password):
        return user
    
def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)
