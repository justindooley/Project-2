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
engine1 = create_engine("mysql://root:password@localhost/beer_db")
engine2 = create_engine("mysql://root:password@localhost/beer_review_db")
engine3 = create_engine("mysql://root:password@localhost/beer_adv_db")

# Query the db to Pandas
data1 = pd.read_sql_query("SELECT * FROM beer_data", con = engine1)
data2 = pd.read_sql_query("SELECT * FROM beer_review", con = engine2)
data3 = pd.read_sql_query("SELECT * FROM beer_advocate_data", con = engine3)

# Test Pandas_df
# print(data2.head())

# Dataframe to JSON
data_all1 = data1.to_json(orient='records')
data_names1 = data1["Name"].to_json(orient='columns')
data_all2 = data2.to_json(orient='records')
data_names2 = data2["beer_name"].to_json(orient='columns')
data_all3 = data3.to_json(orient='records')
data_names3 = data3["Name"].to_json(orient='columns')

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
        f"<h1>Welcome to Our ETL Project Flask App</h1>"
        f"<br/>"
        f"<img src=""https://www.maxim.com/.image/t_share/MTQ2ODUxNjY1ODIyMDk4OTgw/two-pints-beer-main.jpg"" alt=""two-pints-beer-main"" width=""250"" height=""250""><br/>"
        f"<br/>"
        f"Available Routes for BreweryDB Data:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/all<br/>"
        f"<br/>"
        f"Available Routes for BeerAdvocate Data:<br/>"
        f"/api/v1.0/names2<br/>"
        f"/api/v1.0/all2<br/>"
        f"<br/>"
        f"Available Routes for BeerAdvocate Data Top 50 (Webscraping):<br/>"
        f"/api/v1.0/names3<br/>"
        f"/api/v1.0/all3<br/>"
    )

@app.route("/api/v1.0/names")
def names1():
    return data_names1

@app.route("/api/v1.0/all")
def data1():
    return data_all1

@app.route("/api/v1.0/names2")
def names2():
    return data_names2

@app.route("/api/v1.0/all2")
def data2():
    return data_all2

@app.route("/api/v1.0/names3")
def names3():
    return data_names3

@app.route("/api/v1.0/all3")
def data3():
    return data_all3

if __name__ == '__main__':
    app.run(debug=True)
