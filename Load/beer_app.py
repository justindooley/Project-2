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
        f"/api/v1.0/beer_dbs"
    )

@app.route("/api/v1.0/names")
def names():
    """Return a list of all beer_db names"""
    return data_names



@app.route("/api/v1.0/all")
def beer_dbs():
    return data_all

# @app.route("/api/v1.0/beer_dbs")
# def beer_dbs():
    """Return a list of beer_db data including the name, age, and sex of each beer_db"""
    # Query all beer_dbs
    # results = session.query(Beer_db).all()

    # Create a dictionary from the row data and append to a list of all_beer_dbs
    # all_beer_dbs = []
    # for beer_db in data:
    #     beer_db_dict = {}
    #     beer_db_dict["ID"] = data['ID']
    #     beer_db_dict["Name"] = data['Name']
    #     beer_db_dict["ABV"] = data['ABV']
    #     beer_db_dict["Style"] = data['Style']
    #     beer_db_dict["Is Retired"] = beer_db['Is Retired']
    #     all_beer_dbs.append(beer_db_dict)

    # return jsonify(all_beer_dbs)

if __name__ == '__main__':
    app.run(debug=True)
