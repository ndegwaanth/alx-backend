#!/usr/bin/env python3
"""2-app.py basic flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Function to select the best match locale from the request.

    Returns:
        The best match locale from the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Homepage of the 2-index.html"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
