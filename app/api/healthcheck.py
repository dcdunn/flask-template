from flask import jsonify
from . import api

HEALTHCHECK_OK = {
    "data" : {
        "type": "healthcheck"
    }
}

@api.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify(HEALTHCHECK_OK), 200

