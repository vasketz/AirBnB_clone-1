#!/usr/bin/python3
"""
This script starts a flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Funtion to print Hello HBNB!
    """
    return "Hello_HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
