from os import environ

class Config:
    ######################### global Configuration #########################
    ENV = environ.get("TOYBOX_AYTHZ_ENV","production")
    DEBUG = bool(int(environ.get("TOYBOX_AYTHZ_DEBUG","0")))
    TESTING = bool(int(environ.get("TOYBOX_AYTHZ_TESTING","0")))
    SECRET_KEY = environ.get("TOYBOX_AUTHZ_SECRET_KEY", "HARD_STRONG_SECRET_KEY")
    JSONIFY_PRETTYPRINT_REGULAR = True
    
    ######################### Database Configuration #########################
    SQLALCHEMY_DATABASE_URI = environ.get("TOYBOY_AUTHZ_DATABASE_URI",None)
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    