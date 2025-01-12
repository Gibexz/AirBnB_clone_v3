#!/usr/bin/python3
"""
module: app.py
"""

from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def teardown(exception):
    """teardown context to close the session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """function to return error 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """ main function """
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
