from flask import Flask, jsonify
from flask_cors import CORS
#from package import ebook

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

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
    import ebook
    import ebooklib
    ebook.read()
    return {"greeting": "Hi!!!!"}


if __name__ == '__main__':
    app.run()