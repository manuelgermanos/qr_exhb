from flask import Flask, jsonify , session
from pymongo import MongoClient



app = Flask(__name__)
app.secret_key = 'seb5goat'

# Define the MongoDB connection string
connection_string = "mongodb+srv://rec1:rec1@coe416database.qlhbx66.mongodb.net/"

# Connect to the MongoDB cluster
client = MongoClient(connection_string)

# Select the database and collections to use
db = client.f1_2
drivers_collection = db.drivers
drivesFor_collection = db.drivesFor
rec1_collection = db.rec1
constructors_collection = db.constructors


@app.route('/constructor/<constID>')
def constructor(constID):
    # Select the database and collections to use
    db = client.f1_2
    constructors = db.constructors
    drivesFor = db.drivesFor
    drivers = db.drivers
    rec1 = db.rec1

    # Retrieve the details of the selected constructor
    constructor_data = constructors.find_one({'constID': constID}, {'_id': 0})
    if constructor_data is None:
        return jsonify({'error': 'Invalid constID'}), 400

    # Retrieve the drivers that drive for the selected constructor
    drivesFor_data = list(drivesFor.find({'constID': constID}, {'_id': 0, 'driverID': 1}))

    # Retrieve the details of the drivers
    drivers_data = []
    for driveFor in drivesFor_data:
        driver_data = drivers.find_one({'driverID': driveFor['driverID']}, {'_id': 0})
        if driver_data is not None:
            drivers_data.append(driver_data)

    # Check if there is a previously selected constructor in the session
    prev_constID = session.get('prev_constID')

    # If there is a previously selected constructor, increment the corresponding record in the rec1 collection
    if prev_constID is not None and prev_constID != constID:
        trans = f"{prev_constID}xx{constID}"
        rec1.update_one({'trans': trans}, {'$inc': {'num': 1}}, upsert=True)
    doc = db.rec2.find_one({'picked': constID})
    if doc is not None:
        db.rec2.update_one({'_id': doc['_id']}, {'$inc': {'num1': 1}})

    # Store the current constructor in the session
    session['prev_constID'] = constID

    # Combine the data into a single dictionary
    data = {
        'constructor': constructor_data,
        'drivers': drivers_data,
    }

    # Return the data as JSON
    return jsonify(data)




if __name__ == '__main__':
    app.run()
