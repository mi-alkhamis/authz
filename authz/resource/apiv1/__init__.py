from authz.authz import apiv1 as api  # refers to apiv1 in authz file
from authz.resource.apiv1.user import UserResource
from authz.resource.apiv1.auth import AuthTokenResource


api.add_resource(
    AuthTokenResource, "/auth/tokens", methods=["GET", "POST"], endpoint="auth_tokens"
)


api.add_resource(UserResource, "/users", methods=["GET", "POST"], endpoint="users")

api.add_resource(
    UserResource,
    "/users/<user_id>",  # can set <user_id>:string|int|uuid...
    methods=["GET", "PATCH", "DELETE"],
    endpoint="user",
)
