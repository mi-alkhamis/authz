from authz.util import jsonify, now
from authz.authz import db
from authz.schema.apiv1 import UserSchema
from authz.model import User
from flask import request


class UserController:
    def get_user_list():

        try:
            users = User.query.all()  # Query users from  db
        except:
            return jsonify(status=500, code=102)
        users_schema = UserSchema(many=True)  # Create user list serialization object
        return jsonify({"Users": users_schema.dump(users)})  # Returm list of users

    def get_user(user_id):
        try:
            user = User.query.get(user_id)  # Return a user
        except:
            return jsonify(status=500, code=102)  # Database error
        if user is None:
            return jsonify(status=404, code=103)  # User is not found
        user_schema = UserSchema()
        return jsonify({"User": user_schema.dump(user)})  # Return a user

    def create_user():

        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())  # Validate User Data
        except:
            return jsonify(status=400, code=104)  # Validation Failed
        if not data["username"] or not data["password"]:  # check for non empty fields
            return jsonify(status=400, code=105)
        try:
            user = User.query.filter_by(
                username=data["username"]
            ).first()  # Check for username Duplication
        except:
            return jsonify(status=500, code=102)  # Database Error
        if user is not None:
            return jsonify(status=409, code=106)  # Resource Conflict
        user = User(username=data["username"], password=data["password"])
        db.session.add(user)  # Select user for inserting into db
        try:
            db.session.commit()  # Insert USER into DB
        except:
            db.session.rollback()  # Rollback  if has a db error
            return jsonify(status=500, code=102)  # Database Error
        user_schema = UserSchema()
        return jsonify(
            {"User": user_schema.dump(user)}, status=201
        )  # Return a new user

    def update_user(user_id):
        user_schema = UserSchema(only=["password"])

        try:
            data = user_schema.load(request.get_json())  # Validate User Data
        except:
            return jsonify(status=400, code=104)  # Validation Failed
        if not data["password"]:  # check for non empty fields
            return jsonify(status=400, code=105)
        try:
            user = User.query.get(user_id)  # Select user
        except:
            return jsonify(status=500, code=102)  # Database Error
        if user is None:
            return jsonify(status=404, code=103)  # User is not found

        user.password = data["password"]
        user.last_change_at = now()
        db.session.add(user)
        try:
            db.session.commit()  # update user's password  in database
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        user_schema = UserSchema()
        return jsonify({"user": user_schema.dump(user)})

    def delete_user(user_id):
        try:
            user = User.query.get(user_id)  # Select user
        except:
            return jsonify(status=500, code=102)  # Database Error
        if user is None:
            return jsonify(status=404, code=103)  # User is not found
        db.session.delete(user)
        try:
            db.session.commit()  # update user's password  in database
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        return jsonify()
