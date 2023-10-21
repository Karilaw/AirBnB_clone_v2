#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route to display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route to display 'C ', followed by the variable.
    Replace underscore _ symbols with a space.
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route to display 'Python ', followed by the value.
    Replace underscore _ symbols with a space.
    The default value of text is 'is cool'.
    """
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    """Main method that starts the Flask web application"""
    app.run(host='0.0.0.0', port=5000)
