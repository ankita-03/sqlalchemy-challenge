# I am having some troulbes with the last part, I was not able to finish on time. Is it possible I can resubmit this after completing it properly.   


import numpy as np 
import pandas as pd
import datetime as dt
import sqlalchemy
import flask import Flask, jsonify 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect an exisiting database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)
# Last Date ?
#session.query(func.max(measurement.date)).first()[0]

app = Flask(_name_)

# Navigation
@app.route("/")
def home():
    return (
        f"<h1>Welcome to CLIMATE APP API</h1>"
        f"Routes:<br/>"
        f"Precipitation Data</br>"
        f"/api/v1.0/precipitation<br/>"
        f"Station Data</br>"
        f"/api/v1.0/stations<br/>"
        f"Tempreture Observation Data</br>"
        f"/api/v1.0/tobs<br/>"
        f"Start Date</br>"
        f"/api/v1.0/<start><br/>"
        f"Start and End Date<br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Route 1
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    prcp_data = session.query(measurement.date, measurement.prcp).all()
    session.close()

    precipitation = [] #dictionary 
    for date, prcp in prcp_data:
        dict1 = {}
        dict1["date"] = prcp_data[0]
        dict1["prcp"] = prcp_data[1]
        precipitation.append(dict1)
    return jsonify(precipitation)

# Route 2
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_data = session.query(station.station, station.name).all()
    session.close()

    stat = [] #dictionary 
    for station, name in station_data:
        dict2 = {}
        dict2["station"] = station_data[0]
        dict2["name"] = station_data[1]
        stat.append(dict2)
    return jsonify(stat)

# Route 3
@app.route("/api/v1.0/tobs")
def tobs
    session = Session(engine)
    temp_route = session.query(measurement.tobs, measurement.date).filter(measurement.date >= '2016-08-23').all()
    session.close()

    tob_data = [] #dictionary 
    for tobs, date in temp_route
        dict3 = {}
        dict3["tobs"] = temp_route[0]
        dict3["date"] = temp_route[1]
        tob_data.append(dict3)
    return jsonify(tob_data)

# Route 4
#@app.route("/api/v1.0/<start>")
#def start_temperature(start):
   # session = Session(engine)



