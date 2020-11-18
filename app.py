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

#API START AND API END
#Define function for querying based on start date, and returning TMAX, TMIN, and TAVG
def start_temps_calc(start_date):

    session = Session(engine)

    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

#Set app route and create dictionary for query values, and jsonify the dictionary response
@app.route("/api/v1.0/<start>")
def start_date(start):
    starting_temp = start_temps_calc(start)
    temps = list(np.ravel(starting_temp))
    
    min_temp = temps[0]
    avg_temp = temps[1]
    max_temp = temps[2]
    temp_dict = {'Min Temp': min_temp, 'Max Temp': max_temp, 'Avg Temp': avg_temp, 'Start Date': start}

    return jsonify(temp_dict)

#Define function for querying based on start and end date, and returning TMIN, TMAX, and TAVG
def temps_calc(start_date, end_date):
    session = Session(engine)

    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

#Set app route and create dictionary for query values, and jsonify response
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    start_end_temps = temps_calc(start, end)
    all_temps = list(np.ravel(start_end_temps))

    min_t = all_temps[0]
    avg_t = all_temps[1]
    max_t = all_temps[2]
    all_temp_dict = {'Min Temp': min_t, 'Max Temp': max_t, 'Avg Temp': avg_t, 'Start Date': start, 'End Date': end}

    return jsonify(all_temp_dict)
     
    

if __name__ == '__main__':
    app.run(debug=True)