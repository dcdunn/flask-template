from . import api

@api.route('/healthcheck', methods=['GET'])
def healthcheck():
    return "", 200

