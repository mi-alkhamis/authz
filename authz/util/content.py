from flask import Flask, request
from authz.util import jsonify
from authz.config import Config


def check_request_content_type():
    if request.content_type != "application/json":
        return jsonify(status=415, code=101)
