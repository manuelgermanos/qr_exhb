from flask import Flask, jsonify, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'seb5goat'

connection_string = "mongodb+srv://rec1:rec1@coe416database.qlhbx66.mongodb.net/"

client = MongoClient(connection_string)

db = client.f1_2
drivers_collection = db.drivers
drivesFor_collection = db.drivesFor
rec1_collection = db.rec1
constructors_collection = db.constructors


@app.route('/constructor/<constID>')
def constructor(constID):
    db = client.f1_2
    constructors = db.constructors
    drivesFor = db.drivesFor
    drivers = db.drivers
    rec1 = db.rec1

    constructor_data = constructors.find_one({'constID': constID}, {'_id': 0})
    if constructor_data is None:
        return jsonify({'error': 'Invalid constID'}), 400

    drivesFor_data = list(drivesFor.find({'constID': constID}, {'_id': 0, 'driverID': 1}))

    drivers_data = []
    for driveFor in drivesFor_data:
        driver_data = drivers.find_one({'driverID': driveFor['driverID']}, {'_id': 0})
        if driver_data is not None:
            drivers_data.append(driver_data)

    prev_constID = session.get('prev_constID')

    if prev_constID is not None and prev_constID != constID:
        trans = f"{prev_constID}xx{constID}"
        rec1.update_one({'trans': trans}, {'$inc': {'num': 1}}, upsert=True)
    doc = db.rec2.find_one({'picked': constID})
    if doc is not None:
        db.rec2.update_one({'_id': doc['_id']}, {'$inc': {'num1': 1}})

    session['prev_constID'] = constID

    data = {
        'constructor': constructor_data,
        'drivers': drivers_data,
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run()