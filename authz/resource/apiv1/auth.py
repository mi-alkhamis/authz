from flask_restful import Resource
from authz.controller.apiv1 import AuthTokenController


class AuthTokenResource(Resource):
    def get(self):
        """
        GET /auth/tokens --> Verify User JWT tokens
        """
        return AuthTokenController.verify_jwt_token()  # Verify User JWT tokens

    def post(self):
        """
        POST /auth/tokens --> Create User JWT token for user
        """
        return AuthTokenController.create_jwt_token()  # Create User JWT token for user
