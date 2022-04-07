from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


from authz.config import Config
db = SQLAlchemy()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1", __name__, url_prefix = "/api/v1")
apiv1 = Api(apiv1_bp)

from authz import resource # must be located here, after apiv1

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Load Config from environments variables
    db.init_app(app) # init SQLAlchemy Database object
    ma.init_app(app)
    app.register_blueprint(apiv1_bp)
    return app