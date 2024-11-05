#!/usr/bin/env python3
<<<<<<< HEAD
"""
A Basic flask application
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
=======
"""A Basic Flask app.
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """The home/index page.
>>>>>>> 87993d5e35a2385b0b11eb172faf9ee70c2087a7
    """
    return render_template('1-index.html')


if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 87993d5e35a2385b0b11eb172faf9ee70c2087a7
