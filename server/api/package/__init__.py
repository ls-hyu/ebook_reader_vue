from flask import Flask, jsonify
from flask_cors import CORS
#from package import ebook

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#from package import routes
from . import routes
#from package import ebook
#import ebooklib