#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """Displays an HTML page like 6-index.html."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('10-hbnb_filters.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
