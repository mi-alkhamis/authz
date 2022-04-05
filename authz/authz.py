from flask import Flask, Blueprint
from flask_restful import Api

from authz.config import Config

apiv1_bp = Blueprint("apiv1", __name__, url_prefix = "/api/v1")
apiv1 = Api(apiv1_bp)

from authz import resource # must be located here, after apiv1

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Load Config from environments variables
    app.register_blueprint(apiv1_bp)
    return app