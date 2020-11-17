import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect existing database into new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#Save references to the two tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#Setup Flask
app = Flask(__name__)

#Flask Routes

@app.route("/")
def home():
    """List all available routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

#Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create out session link from Python to the DB
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    #Convert the query results to a dictionary using date as the key and prcp as the value
    all_measurements = []
    for date, prcp in results:
        measurement_dict = {"Date":"Precipitation"}
        measurement_dict["Date"] = date
        measurement_dict["Precipitation"] = prcp
        all_measurements.append(measurement_dict)

    return jsonify(all_measurements)

#Station
@app.route("/api/v1.0/stations")
def stations():
    #Create out session link from Python to the DB
    session = Session(engine)

    #Return a JSON list of stations from the dataset
    results = session.query(Station.station).all()

    session.close()

    return jsonify(results)
    
if __name__ == '__main__':
    app.run(debug=True)