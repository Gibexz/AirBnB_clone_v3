#!/usr/bin/python3
"""
module: index.py
"""

from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    """ Returns the status of the page """
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def objCount():
    """ Returns the number of each objects in storage """
    storage.reload()

    return jsonify({
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User)
        })
