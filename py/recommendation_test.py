from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Define the MongoDB connection string
connection_string = "mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/"

# Connect to the MongoDB cluster
client = MongoClient(connection_string)

# Select the database and collections to use
db = client.f1_2
drivers_collection = db.drivers
drivesFor_collection = db.drivesFor
rec1_collection = db.rec1
constructors_collection = db.constructors


@app.route('/constructor/<constID>')
def get_constructor(constID):
    # Select the database and collections to use
    db = client.f1_2
    constructors = db.constructors
    drivesFor = db.drivesFor
    drivers = db.drivers

    # Retrieve the constructor with the given constID
    constructor = constructors.find_one({'constID': constID}, {'_id': 0})

    if constructor:
        # Retrieve the drivers that drive for this constructor
        driverIDs = [d['driverID'] for d in drivesFor.find({'constID': constID}, {'_id': 0})]
        driver_docs = drivers.find({'driverID': {'$in': driverIDs}}, {'_id': 0})
        drivers_data = list(driver_docs)

        # Add the drivers data to the constructor dictionary
        constructor['drivers'] = drivers_data

        # Return the data as JSON
        return jsonify(constructor)
    else:
        # Return a 404 error if the constructor is not found
        return jsonify({'error': 'Constructor not found'}), 404


@app.route('/')
def index():
    # Create links to the different endpoints
    links = {
        'all_drivers': '/drivers',
        'all_constructors': '/constructors',
        'constructor': '/constructor/<constID>'
    }

    # Return the links as JSON
    return jsonify(links)



if __name__ == '__main__':
    app.run()
