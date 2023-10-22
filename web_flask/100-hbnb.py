#!/usr/bin/python3
""" Full web static and Dynamic """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb')
def hbnb():
    """
    Route that displays a HTML page with states, amenities, and places
    loaded from a storage engine.
    """
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    places = storage.all('Place').values()
    places = sorted(places, key=lambda place: place.name)
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Method to handle teardown of the SQLAlchemy Session after each request.
    """
    storage.close()

if __name__ == '__main__':
    """
    Main driver function for the Flask web application.
    """
    app.run(host='0.0.0.0', port=5000)
