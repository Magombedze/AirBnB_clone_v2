#!/usr/bin/python3
"""It starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask('web_flask')


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)



@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

