import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float 

# Import Flask
from flask import Flask, jsonify

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

#################################################
# Database Setup
#################################################

# Create engine
engine = create_engine("mysql://root:password@localhost/beerdb")

# Query the db to Pandas
data = pd.read_sql_query("SELECT * FROM beer_data1", con = engine)

# Test Pandas_df
print(data.head())

# Dataframe to JSON
data_all = data.to_json(orient='records')
data_names = data["Name"].to_json(orient='columns')

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
        f"Available Routes:><br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/all<br/>"
    )

@app.route("/api/v1.0/names")
def names():
    """Return a list of all beer_db names"""
    return data_names


@app.route("/api/v1.0/all")
def beer_dbs():
    return data_all


if __name__ == '__main__':
    app.run(debug=True)
