from os import environ


class Config:
    ######################### global Configuration #########################
    ENV = environ.get("TOYBOX_AYTHZ_ENV", "production")
    DEBUG = bool(int(environ.get("TOYBOX_AYTHZ_DEBUG", "0")))
    TESTING = bool(int(environ.get("TOYBOX_AYTHZ_TESTING", "0")))
    # at least 256 chars and complex for production
    SECRET_KEY = environ.get("TOYBOX_AUTHZ_SECRET_KEY", "HARD_STRONG_SECRET_KEY")
    JSONIFY_PRETTYPRINT_REGULAR = True
    TIMEZONE = environ.get("TOYBOY_AUTHZ_TIMEZONE", "Asia/Tehran")

    ######################### Database Configuration #########################
    SQLALCHEMY_DATABASE_URI = environ.get("TOYBOY_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

    ########################### User Configuration ###########################
    USER_DEFAULT_EXPIRES_TIME = int(
        environ.get("TOYBOX_AUTHZ_USER_DEFAULT_EXPIRES_TIME", "365")
    )
    USER_DEFAULT_ROLE = environ.get("TOYBOX_AUTHZ_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_STATUS = int(environ.get("TOYBOX_AUTHZ_USER_DEFAULT_STATUS", "0"))

    ####################### Authentication Configuration ######################
    JWT_TOKEN_DEFAULT_EXPIRY_TIME = int(
        environ.get("TOYBOX_AUTHZ_JWT_TOKEN_DEFAULT_EXPIRY_TIME", "86400")
    )
    JWT_TOKEN_DEFAULT_ALGORITHM = environ.get(
        "TOYBOX_AUTHZ_JWT_TOKEN_DEFAULT_ALGORITHM", "HS512"
    )
