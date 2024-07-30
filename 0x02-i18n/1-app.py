#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
The application uses Flask-Babel for internationalization support.
"""

from flask import Flask, render_template
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


# Apply the configuration to the Flask app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@app.route('/')
def index():
    """
    Route for the home page.

    Returns:
        A rendered HTML template with a welcome message.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
