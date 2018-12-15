import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sql:///beer_data.sql")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Beer_db = Base.classes.beer_db

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/beer_dbs"
    )

@app.route("/api/v1.0/names")
def names():
    """Return a list of all beer_db names"""
    # Query all beer_dbs
    results = session.query(Beer_db.name).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/beer_dbs")
def beer_dbs():
    """Return a list of beer_db data including the name, age, and sex of each beer_db"""
    # Query all beer_dbs
    results = session.query(Beer_db).all()

    # Create a dictionary from the row data and append to a list of all_beer_dbs
    all_beer_dbs = []
    for beer_db in results:
        beer_db_dict = {}
        beer_db_dict["ID"] = beer_db.id
        beer_db_dict["Name"] = beer_db.name
        beer_db_dict["ABV"] = beer_db.abv
        beer_db_dict["Style"] = beer_db.style
        beer_db_dict["Is Retired"] = beer_db.isretired
        all_beer_dbs.append(beer_db_dict)

    return jsonify(all_beer_dbs)

if __name__ == '__main__':
    app.run(debug=True)
