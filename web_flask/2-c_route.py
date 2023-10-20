#!/usr/bin/python3
""" A module that defines flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when the root URL is requested."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when the '/hbnb' URL is requested."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C ' followed by the value of the te."""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
