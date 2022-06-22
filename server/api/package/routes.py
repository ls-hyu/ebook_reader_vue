from flask import jsonify
from flask_cors import CORS
#from package import app
from . import app
#from package import ebook
#from . import ebook

# enable CORS/Cross-Origin Resource Sharing, allows the request from different origins
CORS(app, resources={r'/*': {'origins': '*'}}) # set origins to * means the wildcard for all the origins

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/greeting')
def greeting():
    #from .ebook import read
    #read()
    #from api.test import api
    from . import ebook
    ebook.read()
    return {"greeting": "Hi!!!!"}