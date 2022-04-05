
from flask import current_app

DEBUG_MSG_CODES = {
    "100":"OK"
    
}

def jsonify (state={}, metadata={}, status=200, code=100, headers={}):
    data = state
    data.update(metadata)
    if current_app.debug:
        data["MESSAGES"] = DEBUG_MSG_CODES[str(code)]
    data["code"] = code
    return data, status, headers