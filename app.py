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
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )