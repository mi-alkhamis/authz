from authz.util import jsonify
from authz.schema.apiv1 import UserSchema
from authz.model import User

class UserController:
    
    def get_user_list():
        return jsonify(status=501)

    def crate_user():
        return jsonify(status=501)
    
    def get_user(user_id):
        return jsonify(status=501)
    
    def update_user(user_id):
        return jsonify(status=501)
    
    def delete_user(user_id):
        return jsonify(status=501)