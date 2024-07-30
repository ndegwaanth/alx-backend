#!/usr/bin/env python3
"""0-basic flask application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """render the index.html file to the browser"""
    return render_template('index.html')


if __name__ == "__main__":
    """main entry of the code"""

    app.run(debug=True)
