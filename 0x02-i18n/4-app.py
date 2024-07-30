#!/usr/bin/env python3
"""
A basic Flask app with Babel for internationalization.

This script sets up a Flask application with Babel to handle
translations based on the user's locale. The available languages
are English and French, and the default locale and timezone are
set to English and UTC, respectively.

Additionally, it allows forcing a particular locale by passing
the 'locale' parameter in the URL.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


# Instantiate the Babel object
babel = Babel(app)


class Config:
    """
    Config class to store configuration variables.

    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the configuration to the Flask app
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.

    This function checks if the 'locale' parameter is present in the request
    and if its value is a supported locale. If so, it returns that locale.
    Otherwise, it uses the 'Accept-Language' header from the request to
    determine the best match from the supported languages.

    Returns:
        str: The best match locale.
    """
    # Check if 'locale' parameter is present in the request
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    # Run the Flask app in debug mode

    app.run(debug=True)
