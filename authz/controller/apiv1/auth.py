from authz.util import jsonify, now
from authz.authz import db
from authz.schema.apiv1 import UserSchema
from authz.model import User
from flask import request
from jwt import encode, decode
from authz.config import Config
from datetime import datetime
from time import time


class AuthTokenController:
    def verify_jwt_token():
        return jsonify(status=501, code=107)

    def create_jwt_token():

        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())  # Validate User Data
        except:
            return jsonify(status=400, code=104)  # Validation Failed
        if not data["username"] or not data["password"]:  # check for non empty fields
            return jsonify(status=400, code=105)
        try:
            user = User.query.filter_by(username=data["username"]).first()
            # Check for username Duplication
        except:
            return jsonify(status=500, code=102)  # Database Error
        if user is None:
            return jsonify(status=403, code=103)  # User is not found(Access Denied!)
        if user.password == data["password"]:
            if user.expires_at < now():
                return jsonify(status=403, code=108)  # user is expired
            if user.status != 3:
                return jsonify(status=403, code=109)  # user has not desired status
            current_datetime = now()
            current_time = time()
            try:
                user_jwt_token = encode(
                    {
                        "user": {
                            "id": user.id,
                            "username": user.username,
                            "role": user.role,
                            "expires_at": datetime.isoformat(user.expires_at),
                        },
                        "sub": user.id,
                        "nbf": current_time,
                        "exp": current_time + Config.USER_DEFAULT_EXPIRES_TIME,
                    },
                    Config.SECRET_KEY,
                    Config.JWT_TOKEN_DEFAULT_ALGORITHM,
                ).encode(
                    "utf8"
                )  # Create new JWT token
            except Exception as e:
                print(e)
                return jsonify(status=500, code=110)
            user.last_login_at = current_datetime  # update last login at time
            try:
                db.session.commit()  # update Database command
            except:
                db.session.rollback()  # Rollback changes
                return jsonify(status=500, code=102)  # Database Error
            user_schema = UserSchema()
            return jsonify(
                {"user": user_schema.dump(user)},
                status=201,
                headers={"X-Subject-Token": user_jwt_token},  # Best Practice to use it
            )

        else:
            user.failed_auth_at = now()
            user.failed_auth_count = +1
            try:
                db.session.commit()  # update Database command
            except:
                db.session.rollback()  # Rollback changes
                return jsonify(status=500, code=102)  # Database Error
            return jsonify(status=403, code=111)  # incorrect user and password
