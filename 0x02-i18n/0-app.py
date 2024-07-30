#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """This function render the index.html file"""
    return render_template('index.html')


if __name__ == '__main__':
    """This is the entry point of the application"""
    app.run(debug=True)
