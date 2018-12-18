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
engine1 = create_engine("mysql://root:password@localhost/beerdb")
engine2 = create_engine("mysql://root:password@localhost/beer_review_db)")

# Query the db to Pandas
data1 = pd.read_sql_query("SELECT * FROM beer_data1", con = engine1)
data2 = pd.read_sql_query("SELECT * FROM beer_review", con = engine2)

# Test Pandas_df
print(data2.head())

# Dataframe to JSON
data_all = data1.to_json(orient='records')
data_names1 = data1["Name"].to_json(orient='columns')
data_names2 = data2["brewery_id"].to_json(orient='columns')

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

@app.route("/api/v1.0/names1")
def names():
    """Return a list of all beer_db names"""
    return data_names1


@app.route("/api/v1.0/all")
def beer_dbs():
    return data_all

@app.route("/api/v1.0/names2")
def names():
    """Return a list of all beer_db names"""
    return data_names2

if __name__ == '__main__':
    app.run(debug=True)
