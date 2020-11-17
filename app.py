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
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
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

#TOBS
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    #Query the dates and temperature observations of the most active station for the last year of data
    results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date <= '2017-08-23').\
            filter(Measurement.date >= '2016-08-23').\
            filter(Measurement.station == 'USC00519281').all()

    session.close()

    return jsonify(results)

# #API START AND API END
# @app.route("/api/v1.0/<start>")
# def temp_by_start_date(Date):
#     """Return a JSON list of TMIN, TAVG, and TMAX for all dates greater than
#         or equal to the start date"""
#     canonicalized = Date
#     for date in all_measurements:
#         search_term = date["Date"]

#         if search_term == canonicalized:
#             return jsonify(func.max(Measurement.tobs))
#             return jsonify(func.min(Measurement.tobs))
#             return jsonify(func.avg(Measurement.tobs))

if __name__ == '__main__':
    app.run(debug=True)