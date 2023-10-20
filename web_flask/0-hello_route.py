#!/usr/bin/python3
""" A module tht starts web flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!' when the user visits the route '/'

    Returns:
        str: A string containing the message 'Hello HBNB!'
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
